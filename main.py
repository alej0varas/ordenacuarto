#!/bin/env/python
# ordenacuarto helps you to visualize how you can locate your furniture in your room

import sys, pygame


DEFAULT_BOX_SIZE = (40, 40)


class Main:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = (640, 480)#pygame.display.list_modes()[0]
        self.screen = pygame.display.set_mode(self.size)

        self.background = pygame.surface.Surface(self.size)
        self.background.fill(pygame.color.THECOLORS['black'])

        self.clicked = False
        self.boxes = pygame.sprite.Group()


        self.get_initial_data()
        self.run()

    def get_initial_data(self):
        # ask user for room size and some day for shape.
        pass

            

    def run(self):
        while 1:
            for event in pygame.event.get():
                #print event
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = False
                elif event.type == pygame.KEYUP:
                    self.create_box()

                if event.type == pygame.MOUSEMOTION and self.clicked:
                    self.mouse_click(event)


            #screen.fill(pygame.color.THECOLORS['black'])
            self.boxes.update()
            self.boxes.clear(self.screen, self.background)
            self.boxes.draw(self.screen)
            pygame.display.flip()

    def mouse_click(self, event):
        for box in self.boxes.sprites():
            if box.rect.collidepoint(event.pos):
                box.rect = box.rect.move(event.rel)
                if box.rect.collidelist([_box.rect for _box in self.boxes.sprites() if _box != box]) >= 0:
                    box.rect = box.rect.move(inverse(event.rel))

    def create_box(self):
        # ask user for:
        # name
        # size
        self.boxes.add(Box())


class Box(pygame.sprite.Sprite):
    def __init__(self, size=DEFAULT_BOX_SIZE):
        super(Box, self).__init__()
        box_surface = pygame.surface.Surface(size)
        box_surface.fill(pygame.color.THECOLORS['white'])

        self.image = box_surface
        self.rect = self.image.get_rect()


# Utils
def inverse(rel):
    return -rel[0], -rel[1]


if __name__ == '__main__':
    Main()
