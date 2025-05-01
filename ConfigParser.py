#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass

# Corrige erro XDG_RUNTIME_DIR e áudio
user = getpass.getuser()
os.environ["XDG_RUNTIME_DIR"] = f"/tmp/runtime-{user}"
os.makedirs(os.environ["XDG_RUNTIME_DIR"], exist_ok=True)
os.chmod(os.environ["XDG_RUNTIME_DIR"], 0o700)
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame, pygame.camera
from pygame.camera import Camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

class CameraDisplay(object):
    def __init__(self, size=(640, 480)):
        self.size = size
        self.display = pygame.display.set_mode(self.size, 0)
        self.framerate = 30
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.main()

    def updateInput(self):
        events = pygame.event.get((pygame.QUIT, pygame.KEYDOWN))
        for event in events:
            if event.type == pygame.QUIT:
                self.going = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    self.going = False

    def updateLogic(self, time):
        pass

    def updateDisplay(self):
        self.snapshot = self.cam.get_image(self.snapshot)
        self.display.blit(self.snapshot, (0, 0))

    def main(self):
        time = 0
        clock = pygame.time.Clock()
        self.going = True
        while self.going:
            time = clock.tick(self.framerate) / 1000.0
            self.updateInput()
            self.updateLogic(time)
            self.updateDisplay()
            pygame.display.flip()
            pygame.event.pump()
        pygame.quit()

def makeCamViewer():
    from multiprocessing import Process
    CamViewer = Process(target=CameraDisplay, name="CamViewer")
    CamViewer.daemon = True
    CamViewer.start()
    return CamViewer

if __name__ == "__main__":
    CamViewer = makeCamViewer()
    CamViewer.join()
