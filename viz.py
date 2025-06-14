import logging

import matplotlib.pyplot as plt
import numpy as np
import imgui
import dnnlib
from imgui_window import imgui_window
from renderer import renderer
from imgui_utils import imgui_utils
from gl_utils import gl_utils
from text_utils import text_utils
from scipy.ndimage import map_coordinates
from muDIC.elements.b_splines import BSplineSurface
from muDIC.elements.q4 import Q4
from viz import renderer
from viz import pickle_widget
from viz import latent_widget
from viz import stylemix_widget
from viz import trunc_noise_widget
from viz import performance_widget
from viz import capture_widget
from viz import backbone_cache_widget
from viz import layer_widget
from viz import pose_widget
from viz import zoom_widget
from viz import conditioning_pose_widget
from viz import render_type_widget
from viz import render_depth_sample_widget

class Fields(object):
    # TODO: Remove Q4 argument. This should be detected automatically
    def __init__(self, dic_results, seed=21, upscale=1, interpolation_order=1):
        self.dic_results = dic_results
        self.seed = seed
        self.upscale = upscale
        self.interpolation_order = interpolation_order

        # Inicialize outros atributos conforme necessário
        # Exemplo:
        # self.generated_field = self.generate_field()

    # Aqui você pode adicionar métodos auxiliares, por exemplo:
    def summary(self):
        return {
            "seed": self.seed,
            "upscale": self.upscale,
            "interpolation_order": self.interpolation_order,
            "keys_in_dic": list(self.dic_results.keys())
        }

    # Exemplo de método gerador (apenas ilustrativo)
    def generate_field(self):
        # lógica de geração com base em dic_results
        """
        Fields calculates field variables from the DIC-results.
        The implementation is lazy, hence getter methods have to be used.

        NOTE
        ----
        The fields are formatted as follows:

        * Vectors: [elm_id,component_i,element_e_coord,element_n_coord,frame_id]
        * matrices: [elm_id,component_i,component_j,element_e_coord,element_n_coord,frame_id]


        Parameters
        ----------
        dic_results :
            The results from the DIC analysis
        seed : Integer
            The number of grid points which will be evaluated in each direction
        upscale : Float
            Return values on a grid upscale times fines than the original mesh

        Returns
        -------
        A Fields object
        """

        self.logger = logging.getLogger()

        # The type is implicitly checked by using the interface
        self.__res__ = dic_results
        self.__settings__ = dic_results.settings
        self.interpolation_order = interpolation_order

        if isinstance(self.__settings__.mesh.element_def, Q4):
            q4 = True
            seed = 1
            self.logger.info("Post processing results from Q4 elements. The seed variable is ignored and the values "
                             "are extracted at the element centers. Use the upscale value to get interpolated fields.")
        else:
            q4 = False
            self.logger.info("Post processing results from B-spline elements. The upscale variable is ignored. Use "
                             "the seed varialbe to set the number of gridpoints to be evaluated along each element "
                             "axis.")

        self.__ee__, self.__nn__ = self.__generate_grid__(seed)

        self.__F__, self.__coords__ = self._deformation_gradient_(self.__res__.xnodesT, self.__res__.ynodesT,
                                                                  self.__settings__.mesh,
                                                                  self.__settings__.mesh.element_def, self.__nn__,
                                                                  self.__ee__)

        # To make the result formatting consistent across element formulations, we arrange the elements onto a grid
        # with the same dimensions as the mesh. If up-scaling is used, we determine the values between element centers
        # by using 3rd order spline interpolation.

        if q4:
            # Flatten things form multiple elements to a grid of elements
            grid_shape = (self.__settings__.mesh.n_ely, self.__settings__.mesh.n_elx)
            n_frames = self.__F__.shape[-1]
            self.__F2__ = np.zeros(
                (1, 2, 2, self.__settings__.mesh.n_elx, self.__settings__.mesh.n_ely, self.__F__.shape[-1]))
            for i in range(2):
                for j in range(2):
                    for t in range(n_frames):
                        self.__F2__[0, i, j, :, :, t] = self.__F__[:, i, j, 0, 0, t].reshape(grid_shape).transpose()

            self.__coords2__ = np.zeros(
                (1, 2, self.__settings__.mesh.n_elx, self.__settings__.mesh.n_ely, self.__F__.shape[-1]))
            for i in range(2):
                for t in range(n_frames):
                    self.__coords2__[0, i, :, :, t] = self.__coords__[:, i, 0, 0, t].reshape(grid_shape).transpose()

            # Overwrite the old results
            # TODO: Remove overwriting results as this is a painfully non-functional thing to do...
            self.__coords__ = self.__coords2__
            self.__F__ = self.__F2__

            self.__coords__ = self.__coords2__
            self.__F__ = self.__F2__

            if upscale != 1.:
                elms_y_fine, elms_x_fine = np.meshgrid(np.arange(0, self.__settings__.mesh.n_elx - 1, 1. / upscale),
                                                       np.arange(0, self.__settings__.mesh.n_ely - 1, 1. / upscale))

                self.__F3__ = np.zeros(
                    (1, 2, 2, elms_x_fine.shape[1], elms_x_fine.shape[0], self.__F__.shape[-1]))

                self.__coords3__ = np.zeros(
                    (1, 2, elms_x_fine.shape[1], elms_x_fine.shape[0], self.__F__.shape[-1]))

                for i in range(2):
                    for t in range(n_frames):
                        self.__coords3__[0, i, :, :, t] = map_coordinates(self.__coords__[0, i, :, :, t],
                                                                          [elms_y_fine.flatten(),
                                                                           elms_x_fine.flatten()],
                                                                          order=self.interpolation_order).reshape(
                            elms_x_fine.shape).transpose()

                for i in range(2):
                    for j in range(2):
                        for t in range(n_frames):
                            self.__F3__[0, i, j, :, :, t] = map_coordinates(self.__F__[0, i, j, :, :, t],
                                                                            [elms_y_fine.flatten(),
                                                                             elms_x_fine.flatten()],
                                                                            order=self.interpolation_order).reshape(
                                elms_x_fine.shape).transpose()

                self.__coords__ = self.__coords3__
                self.__F__ = self.__F3__

    def __generate_grid__(self, seed):

        # TODO: Remove hack:
        if seed == 1:
            return np.meshgrid(np.array([0.5]),
                               np.array([0.5]))

        else:

            if np.ndim(seed) == 1:
                return np.meshgrid(np.linspace(0., 1., seed[0]),
                                   np.linspace(0., 1., seed[1]))

            else:
                return np.meshgrid(np.linspace(0., 1., seed),
                                   np.linspace(0., 1., seed))

    @staticmethod
    def _deformation_gradient_(xnodesT, ynodesT, msh, elm, e, n):
        """
        Calculate the deformation gradient from the control point positions
        and the element definitions.

        See the paper for the procedure.

        Parameters
        ----------
        xnodesT : ndarray
            Node position in the x direction
        ynodesT : ndarray
            Node position in the y direction
        msh : Mesh
            A Mesh object
        elm : Element
            A Element object containing the element definitions
        e : ndarray
            The e coordinates of the element
        n : ndarray
            The n coordinates of the element
        """

        # Post Processing
        nEl = msh.n_elms
        ne = np.shape(e)[0]
        nn = np.shape(e)[1]

        # Evaluate shape function gradients on grid within element
        Nn = elm.Nn(e.flatten(), n.flatten())
        dfde = elm.dxNn(e.flatten(), n.flatten())
        dfdn = elm.dyNn(e.flatten(), n.flatten())

        Fstack = []
        coord_stack = []

        for el in range(nEl):
            x_crd = np.einsum('ij,jn -> in', Nn, xnodesT[msh.ele[:, el], :])
            y_crd = np.einsum('ij,jn -> in', Nn, ynodesT[msh.ele[:, el], :])
            dxde = np.einsum('ij,jn -> in', dfde, xnodesT[msh.ele[:, el], :])
            dxdn = np.einsum('ij,jn -> in', dfdn, xnodesT[msh.ele[:, el], :])
            dyde = np.einsum('ij,jn -> in', dfde, ynodesT[msh.ele[:, el], :])
            dydn = np.einsum('ij,jn -> in', dfdn, ynodesT[msh.ele[:, el], :])

            c_confs = np.array([[dxde, dxdn], [dyde, dydn]])
            r_conf_inv = np.linalg.inv(np.rollaxis(c_confs[:, :, :, 0], 2, 0))

            Fs = np.einsum('ijpn,pjk->ikpn', c_confs, r_conf_inv)

            Fs = Fs.reshape((2, 2, ne, nn, -1))

            x_crd = x_crd.reshape((ne, nn, -1))
            y_crd = y_crd.reshape((ne, nn, -1))

            Fstack.append(Fs)

            coord_stack.append(np.array([x_crd, y_crd]))

        # Returns F(nElms, i, j, ide, idn , frame), coords(nElms, i, ide, idn , frame)

        return np.array(Fstack), np.array(coord_stack)

    @staticmethod
    def _green_deformation_(F):
        """
        Calculate Green deformation tensor from deformation as G = F^T * F
        :param F:
        :return:
        """
        E11 = F[:, 0, 0, :, :, :] ** 2. + F[:, 0, 1, :, :, :] ** 2.

        E12 = F[:, 0, 0, :, :, :] * F[:, 1, 0, :, :, :] + F[:, 0, 1, :, :, :] * F[:, 1, 1, :, :, :]

        E22 = F[:, 1, 0, :, :, :] ** 2. + F[:, 1, 1, :, :, :] ** 2.

        E = np.array([[E11, E12], [E12, E22]])

        E[E == np.nan] = 0.

        return np.moveaxis(E, 2, 0)

    @staticmethod
    def _green_strain_(F):
        """
        Calculate Green strain tensor from F as G = 0.5*(F^T * F -I)
        :param F: Deformation gradient tensor F_ij on the form [nEl,i,j,...]
        :return: Green Lagrange strain tensor E_ij on the form [nEl,i,j,...]
        """
        E11 = 0.5 * (F[:, 0, 0, :, :, :] ** 2. + F[:, 0, 1, :, :, :] ** 2. - 1.)

        E12 = 0.5 * (F[:, 0, 0, :, :, :] * F[:, 1, 0, :, :, :] + F[:, 0, 1, :, :, :] * F[:, 1, 1, :, :, :])

        E22 = 0.5 * (F[:, 1, 0, :, :, :] ** 2. + F[:, 1, 1, :, :, :] ** 2. - 1.)

        E = np.array([[E11, E12], [E12, E22]])

        E[E == np.nan] = 0.

        return np.moveaxis(E, 2, 0)

    @staticmethod
    def _principal_strain_(G):
        E11 = G[:, 0, 0]
        E12 = G[:, 0, 1]
        E21 = G[:, 1, 0]
        E22 = G[:, 1, 1]

        E_temp = np.moveaxis(G, 1, -1)
        E = np.moveaxis(E_temp, 1, -1)

        eigvals, eigvecs = np.linalg.eig(E)

        # print(np.shape(eigvals))
        # print(np.shape(eigvecs))

        ld1 = np.sqrt(eigvals[:, :, :, :, 0])
        ld2 = np.sqrt(eigvals[:, :, :, :, 1])

        ev1 = eigvecs[:, :, :, :, 0, 0]
        ev2 = eigvecs[:, :, :, :, 0, 1]

        # print(np.shape(eigvals))
        # print(np.shape(eigvecs))
        # print(np.shape(ld1))
        # print(np.shape(ev1))

        ld = np.moveaxis(np.array([ld1, ld2]), 0, 1)
        ev = np.moveaxis(np.array([ev1, ev2]), 0, 1)
        print(np.shape(ld1))
        print(np.shape(ev1))

        return ld, ev

    @staticmethod
    def _engineering_strain_(E):
        """
        Calculate engineering strain from Green Lagrange strain tensor E_ij as:
        eps_ii = sqrt(1+E_ii)-1 and
        gamma_ij = 2E_ij/sqrt((1+E_ii)*(1+E_jj))
        :param E: Green Lagrange strain tensor E_ij on the form [nEl,i,j,...]
        :return: Engineering strain tensor eps_ij on the form [nEl,i,j,...]
        """
        eps_xx = np.sqrt(1. + 2. * E[:, 0, 0, :]) - 1.
        eps_yy = np.sqrt(1. + 2. * E[:, 1, 1, :]) - 1.
        eps_xy = 0.5 * np.arcsin(2. * E[:, 0, 1, :] / np.sqrt((1. + 2. * E[:, 0, 0, :]) * (1. + 2. * E[:, 1, 1, :])))

        eps = np.array([[eps_xx, eps_xy], [eps_xy, eps_yy]])

        return np.moveaxis(eps, 2, 0)

    @staticmethod
    def _true_strain_(eps):
        """
        Calculate true strain tensor teps_ij from engineering strain tensor eps_ij as:
        teps_ij = log(eps_ij+1)
        :param eps: Engineering strain tensor eps_ij on the form [nEl,i,j,...]
        :return: True strain tensor teps_ij on the form [nEl,i,j,...]
        """
        return np.log(eps + 1.)

    def true_strain(self):
        E = self._green_strain_(self.__F__)
        engineering_strains = self._engineering_strain_(E)
        return self._true_strain_(engineering_strains)

    def eng_strain(self):
        E = self._green_strain_(self.__F__)
        return self._engineering_strain_(E)

    def F(self):
        return self.__F__

    def green_strain(self):
        return self._green_strain_(self.__F__)

    def coords(self):
        return self.__coords__

    def disp(self):
        return self.__coords__[:, :, :, :, :] - self.__coords__[:, :, :, :, 0, np.newaxis]

    def residual(self, frame_id):
        if self.__settings__.store_internals == False:
            raise ValueError("The analysis has to be run with store_internals=True")
        if isinstance(self.__settings__.mesh.element_def, Q4):
            raise NotImplementedError("Q4 residual fields are not yet implemented")
        ref_id = ind_closest_below(frame_id, [ref.image_id for ref in self.__res__.reference])
        ref = self.__res__.reference[ref_id]

        cross_correlation_product = cross_correlation_products(self.__res__.Ic_stack[frame_id], ref.I0_stack)
        self.logger.info("Cross correlation product is %f" % cross_correlation_product)

        return np.abs(self.__res__.Ic_stack[frame_id] - ref.I0_stack)

    def elm_coords(self, frame_id):
        ref_id = ind_closest_below(frame_id, [ref.image_id for ref in self.__res__.reference])
        ref = self.__res__.reference[ref_id]
        return ref.e, ref.n


class Visualizer(object):
    def __init__(self, fields, images=False):
        """
        Visualizer for field variables.

        Parameters
        ----------
        fields : Fields object
            The Fields object contains all the variables that can be plotted.
        images : ImageStack object
            The stack of images corresponding to Fields

        Returns
        -------
        A Visualizer Object
        """
        if isinstance(fields, Fields):
            self.fields = fields
        else:
            raise ValueError("Only instances of Fields are accepted")

        self.images = images
        self.logger = logging.getLogger()

    def show(self, field="displacement", component=(0, 0), frame=0, quiverdisp=False, **kwargs):
        """
        Show the field variable

        Parameters
        ----------
        field : string
            The name of the field to be shown. Valid inputs are:
                "true strain"
                "eng strain"
                "disp"
                "green strain"
                "residual"

        component : tuple with length 2
            The components of the fields. Ex. (0,1).
            In the case of vector fields, only the first index is used.
        frame : Integer
            The frame number of the field

        """

        keyword = field.replace(" ", "").lower()

        if keyword == "truestrain":
            fvar = self.fields.true_strain()[0, component[0], component[1], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]

        elif keyword in ("F", "degrad", "deformationgradient"):
            fvar = self.fields.F()[0, component[0], component[1], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]

        elif keyword == "engstrain":
            fvar = self.fields.eng_strain()[0, component[0], component[1], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]

        elif keyword in ("displacement", "disp", "u"):
            fvar = self.fields.disp()[0, component[0], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]

        elif keyword in ("coordinates", "coords", "coord"):
            fvar = self.fields.coords()[0, component[0], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]


        elif keyword == "greenstrain":
            fvar = self.fields.green_strain()[0, component[0], component[1], :, :, frame]
            xs, ys = self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame]

        elif keyword == "residual":
            fvar = self.fields.residual(frame)
            xs, ys = self.fields.elm_coords(frame)

        else:
            self.logger.info("No valid field name was specified")
            return

        if np.ndim(fvar) == 2:
            if self.images:
                n, m = self.images[frame].shape
                plt.imshow(self.images[frame], cmap=plt.cm.gray, origin="lower", extent=(0, m, 0, n))

            if quiverdisp:
                plt.quiver(self.fields.coords()[0, 0, :, :, frame], self.fields.coords()[0, 1, :, :, frame],
                           self.fields.disp()[0, 0, :, :, frame], self.fields.disp()[0, 1, :, :, frame],**kwargs)
            else:
                plt.contourf(xs, ys, fvar, 50, **kwargs)
                plt.colorbar()
        plt.show()


def ind_closest_below(value, list):
    ind = 0
    for i, num in enumerate(list):
        if num < value:
            ind = i

    return ind


def cross_correlation_products(field_a, field_b):
    return np.sum(field_a * field_b) / (
            (np.sum(np.square(field_a)) ** 0.5) * (
            np.sum(np.square(field_b)) ** 0.5))
class Visualizer(imgui_window.ImguiWindow):
    def __init__(self, capture_dir=None):
        super().__init__(title='Cat Machine', window_width=3840, window_height=2160)

        # Internals.
        self._last_error_print  = None
        self._async_renderer    = AsyncRenderer()
        self._defer_rendering   = 0
        self._tex_img           = None
        self._tex_obj           = None

        # Widget interface.
        self.args               = dnnlib.EasyDict()
        self.result             = dnnlib.EasyDict()
        self.pane_w             = 0
        self.label_w            = 0
        self.button_w           = 0

        # Widgets.
        self.pickle_widget      = pickle_widget.PickleWidget(self)
        self.latent_widget      = latent_widget.LatentWidget(self)
        self.stylemix_widget    = stylemix_widget.StyleMixingWidget(self)
        self.trunc_noise_widget = trunc_noise_widget.TruncationNoiseWidget(self)
        self.perf_widget        = performance_widget.PerformanceWidget(self)
        self.capture_widget     = capture_widget.CaptureWidget(self)
        self.backbone_cache_widget     = backbone_cache_widget.BackboneCacheWidget(self)
        self.layer_widget       = layer_widget.LayerWidget(self)
        self.pose_widget        = pose_widget.PoseWidget(self)
        self.zoom_widget        = zoom_widget.ZoomWidget(self)
        self.conditioning_pose_widget        = conditioning_pose_widget.ConditioningPoseWidget(self)
        self.render_type_widget = render_type_widget.RenderTypeWidget(self)
        self.render_depth_sample_widget = render_depth_sample_widget.RenderDepthSampleWidget(self)

        if capture_dir is not None:
            self.capture_widget.path = capture_dir

        # Initialize window.
        self.set_position(0, 0)
        self._adjust_font_size()
        self.skip_frame() # Layout may change after first frame.

    def close(self):
        super().close()
        if self._async_renderer is not None:
            self._async_renderer.close()
            self._async_renderer = None

    def add_recent_pickle(self, pkl, ignore_errors=False):
        self.pickle_widget.add_recent(pkl, ignore_errors=ignore_errors)

    def load_pickle(self, pkl, ignore_errors=False):
        self.pickle_widget.load(pkl, ignore_errors=ignore_errors)

    def print_error(self, error):
        error = str(error)
        if error != self._last_error_print:
            print('\n' + error + '\n')
            self._last_error_print = error

    def defer_rendering(self, num_frames=1):
        self._defer_rendering = max(self._defer_rendering, num_frames)

    def clear_result(self):
        self._async_renderer.clear_result()

    def set_async(self, is_async):
        if is_async != self._async_renderer.is_async:
            self._async_renderer.set_async(is_async)
            self.clear_result()
            if 'image' in self.result:
                self.result.message = 'Switching rendering process...'
                self.defer_rendering()

    def _adjust_font_size(self):
        old = self.font_size
        self.set_font_size(min(self.content_width / 120, self.content_height / 60))
        if self.font_size != old:
            self.skip_frame() # Layout changed.

    def draw_frame(self):
        self.begin_frame()
        self.args = dnnlib.EasyDict()
        self.pane_w = self.font_size * 50
        self.button_w = self.font_size * 5
        self.label_w = round(self.font_size * 5.5)

        # Detect mouse dragging in the result area.
        dragging, dx, dy = imgui_utils.drag_hidden_window('##result_area', x=self.pane_w, y=0, width=self.content_width-self.pane_w, height=self.content_height)
        if dragging:
            self.pose_widget.drag(dx, dy)

        # Begin control pane.
        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(self.pane_w, self.content_height)
        imgui.begin('##control_pane', closable=False, flags=(imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE))

        # Widgets.
        expanded, _visible = imgui_utils.collapsing_header('Network & latent', default=True)
        self.pickle_widget(expanded)
        self.pose_widget(expanded)
        self.zoom_widget(expanded)
        self.conditioning_pose_widget(expanded)
        self.render_type_widget(expanded)
        self.render_depth_sample_widget(expanded)
        self.latent_widget(expanded)
        self.stylemix_widget(expanded)
        self.trunc_noise_widget(expanded)
        expanded, _visible = imgui_utils.collapsing_header('Performance & capture', default=True)
        self.perf_widget(expanded)
        self.capture_widget(expanded)
        expanded, _visible = imgui_utils.collapsing_header('Layers & channels', default=True)
        self.backbone_cache_widget(expanded)
        self.layer_widget(expanded)

        # Render.
        if self.is_skipping_frames():
            pass
        elif self._defer_rendering > 0:
            self._defer_rendering -= 1
        elif self.args.pkl is not None:
            self._async_renderer.set_args(**self.args)
            result = self._async_renderer.get_result()
            if result is not None:
                self.result = result

        # Display.
        max_w = self.content_width - self.pane_w
        max_h = self.content_height
        pos = np.array([self.pane_w + max_w / 2, max_h / 2])
        if 'image' in self.result:
            if self._tex_img is not self.result.image:
                self._tex_img = self.result.image
                if self._tex_obj is None or not self._tex_obj.is_compatible(image=self._tex_img):
                    self._tex_obj = gl_utils.Texture(image=self._tex_img, bilinear=False, mipmap=False)
                else:
                    self._tex_obj.update(self._tex_img)
            zoom = min(max_w / self._tex_obj.width, max_h / self._tex_obj.height)
            # print(zoom)
            zoom = np.floor(zoom) if zoom >= 1 else zoom
            # zoom = 1
            self._tex_obj.draw(pos=pos, zoom=zoom, align=0.5, rint=True)
        if 'error' in self.result:
            self.print_error(self.result.error)
            if 'message' not in self.result:
                self.result.message = str(self.result.error)
        if 'message' in self.result:
            tex = text_utils.get_texture(self.result.message, size=self.font_size, max_width=max_w, max_height=max_h, outline=2)
            tex.draw(pos=pos, align=0.5, rint=True, color=1)

        # End frame.
        self._adjust_font_size()
        imgui.end()
        self.end_frame()

#----------------------------------------------------------------------------

class AsyncRenderer:
    def __init__(self):
        self._closed        = False
        self._is_async      = False
        self._cur_args      = None
        self._cur_result    = None
        self._cur_stamp     = 0
        self._renderer_obj  = None
        self._args_queue    = None
        self._result_queue  = None
        self._process       = None

    def close(self):
        self._closed = True
        self._renderer_obj = None
        if self._process is not None:
            self._process.terminate()
        self._process = None
        self._args_queue = None
        self._result_queue = None

    @property
    def is_async(self):
        return self._is_async

    def set_async(self, is_async):
        self._is_async = is_async

    def set_args(self, **args):
        assert not self._closed
        if args != self._cur_args:
            if self._is_async:
                self._set_args_async(**args)
            else:
                self._set_args_sync(**args)
            self._cur_args = args

    def _set_args_async(self, **args):
        if self._process is None:
            self._args_queue = multiprocessing.Queue()
            self._result_queue = multiprocessing.Queue()
            try:
                multiprocessing.set_start_method('spawn')
            except RuntimeError:
                pass
            self._process = multiprocessing.Process(target=self._process_fn, args=(self._args_queue, self._result_queue), daemon=True)
            self._process.start()
        self._args_queue.put([args, self._cur_stamp])

    def _set_args_sync(self, **args):
        if self._renderer_obj is None:
            self._renderer_obj = renderer.Renderer()
        self._cur_result = self._renderer_obj.render(**args)

    def get_result(self):
        assert not self._closed
        if self._result_queue is not None:
            while self._result_queue.qsize() > 0:
                result, stamp = self._result_queue.get()
                if stamp == self._cur_stamp:
                    self._cur_result = result
        return self._cur_result

    def clear_result(self):
        assert not self._closed
        self._cur_args = None
        self._cur_result = None
        self._cur_stamp += 1

    @staticmethod
    def _process_fn(args_queue, result_queue):
        renderer_obj = renderer.Renderer()
        cur_args = None
        cur_stamp = None
        while True:
            args, stamp = args_queue.get()
            while args_queue.qsize() > 0:
                args, stamp = args_queue.get()
            if args != cur_args or stamp != cur_stamp:
                result = renderer_obj.render(**args)
                if 'error' in result:
                    result.error = renderer.CapturedException(result.error)
                result_queue.put([result, stamp])
                cur_args = args
                cur_stamp = stamp

#----------------------------------------------------------------------------

@click.command()
@click.argument('pkls', metavar='PATH', nargs=-1)
@click.option('--capture-dir', help='Where to save screenshot captures', metavar='PATH', default=None)
@click.option('--browse-dir', help='Specify model path for the \'Browse...\' button', metavar='PATH')
def main(
    pkls,
    capture_dir,
    browse_dir
):
    """Interactive model visualizer.

    Optional PATH argument can be used specify which .pkl file to load.
    """
    viz = Visualizer(capture_dir=capture_dir)

    if browse_dir is not None:
        viz.pickle_widget.search_dirs = [browse_dir]

    # List pickles.
    pretrained = [
        'https://api.ngc.nvidia.com/v2/models/nvidia/research/eg3d/versions/1/files/ffhq512-128.pkl',
        'https://api.ngc.nvidia.com/v2/models/nvidia/research/eg3d/versions/1/files/afhqcats512-128.pkl',
        'https://api.ngc.nvidia.com/v2/models/nvidia/research/eg3d/versions/1/files/ffhqrebalanced512-64.pkl',
        'https://api.ngc.nvidia.com/v2/models/nvidia/research/eg3d/versions/1/files/ffhqrebalanced512-128.pkl',
        'https://api.ngc.nvidia.com/v2/models/nvidia/research/eg3d/versions/1/files/shapenetcars128-64.pkl',
    ]

    # Populate recent pickles list with pretrained model URLs.
    for url in pretrained:
        viz.add_recent_pickle(url)

    # Run.
    while not viz.should_close():
        viz.draw_frame()
    viz.close()

#----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
