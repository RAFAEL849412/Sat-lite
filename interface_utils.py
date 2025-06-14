import physics_module as cy
from os.path import dirname, join
from kivy.clock import Clock
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.properties import DictProperty, ListProperty
from kivy.core.image import Image as CoreImage
from random import random
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_string('''
<Playground>:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '40dp'
        TextInput:
            id: search_input
            multiline: False
            hint_text: 'Digite para pesquisar...'
    AsyncImage:
        id: async_img
        source: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzcQpYPzPwiCCsKcZuaT4woGyI_T_DZO0iTQ&s'
        size_hint_y: None
        height: '200dp'
    Label:
        text: 'Circles: %d' % len(root.blist)
''')

class Playground(BoxLayout):
    cbounds = ListProperty([])
    cmap = DictProperty({})
    blist = ListProperty([])

    def __init__(self, **kwargs):
        super(Playground, self).__init__(**kwargs)
        self._hue = 0
        self.init_physics()
        self.bind(size=self.update_bounds, pos=self.update_bounds)
        self.texture = CoreImage(join(dirname(__file__), 'circle.png'), mipmap=True).texture
        Clock.schedule_interval(self.step, 1 / 30.)

    def init_physics(self):
        self.space = cy.Space()
        self.space.iterations = 30
        self.space.gravity = (0, -700)
        self.space.sleep_time_threshold = 0.5
        self.space.collision_slop = 0.5
        for _ in range(4):
            seg = cy.Segment(self.space.static_body, cy.Vec2d(0, 0), cy.Vec2d(0, 0), 0)
            seg.elasticity = 0.6
            self.cbounds.append(seg)
            self.space.add_static(seg)
        self.update_bounds()

    def update_bounds(self, *largs):
        if len(self.cbounds) != 4:
            return
        a, b, c, d = self.cbounds
        x0, y0 = self.pos
        x1 = self.right
        y1 = self.top
        for seg in (a, b, c, d):
            self.space.remove_static(seg)
        a.a, a.b = (x0, y0), (x1, y0)
        b.a, b.b = (x1, y0), (x1, y1)
        c.a, c.b = (x1, y1), (x0, y1)
        d.a, d.b = (x0, y1), (x0, y0)
        for seg in (a, b, c, d):
            self.space.add_static(seg)

    def step(self, dt):
        self.space.step(1 / 30.)
        self.update_objects()

    def update_objects(self):
        for body, obj in self.cmap.items():
            p = body.position
            radius, color, rect = obj
            rect.pos = p.x - radius, p.y - radius
            rect.size = radius * 2, radius * 2

    def add_circle(self, x, y, radius):
        body = cy.Body(100, 1e9)
        body.position = x, y
        circle = cy.Circle(body, radius)
        circle.elasticity = 0.6
        self.space.add(body, circle)
        with self.canvas.before:
            self._hue = (self._hue + 0.01) % 1
            color = Color(self._hue, 1, 1, mode='hsv')
            rect = Rectangle(
                texture=self.texture,
                pos=(self.x - radius, self.y - radius),
                size=(radius * 2, radius * 2))
        self.cmap[body] = (radius, color, rect)
        self.blist.append((body, circle))
        if len(self.blist) > 200:
            old_body, old_circle = self.blist.pop(0)
            self.space.remove(old_body)
            self.space.remove(old_circle)
            radius, color, rect = self.cmap.pop(old_body)
            self.canvas.before.remove(color)
            self.canvas.before.remove(rect)

    def on_touch_down(self, touch):
        self.add_circle(touch.x, touch.y, 10 + random() * 20)

    def on_touch_move(self, touch):
        self.add_circle(touch.x, touch.y, 10 + random() * 20)

class PhysicsApp(App):
    def build(self):
        return Playground()

if __name__ == '__main__':
    PhysicsApp().run()
