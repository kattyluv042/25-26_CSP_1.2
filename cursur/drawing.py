"""
Simple drawing app — pygame canvas with palette, eraser, and brush sizes 1–35.
"""

import pygame
import sys

# --- Palette (order preserved) ---
COLORS = [
    "red",
    "#E68A8D",
    "#AB4543",
    "#9B4443",
    "orange",
    "#EED3B7",
    "#E6B58A",
    "#D35D00",
    "yellow",
    "#EEE1B7",
    "#E6CB8A",
    "#AB9943",
    "green",
    "#BDD299",
    "#7A9B57",
    "#466D1D",
    "#0A2A0A",
    "#A8C1D6",
    "blue",
    "#123456",
    "#40E0D0",
    "#A8AFD6",
    "#4B5390",
    "purple",
    "#BAA8D6",
    "#795CAA",
    "#A858C8",
    "#57357D",
    "pink",
    "#F2799B",
    "#ED408B",
    "#B3394A",
    "grey",
    "#363636",
    "black",
    "#1D1C1C",
]

NAMED_COLORS = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "grey": (128, 128, 128),
    "gray": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}

MIN_BRUSH = 1
MAX_BRUSH = 35
WINDOW_W, WINDOW_H = 1000, 700
CANVAS_H = WINDOW_H - 60
ERASER_BTN = pygame.Rect(20, WINDOW_H - 50, 120, 40)
INSTRUCTIONS = [
    "Draw: click + drag",
    "Space: next color",
    "1: brush size (1–35, wraps)",
    "Eraser: button below",
]


def parse_color(value: str) -> tuple[int, int, int]:
    key = value.strip().lower()
    if key in NAMED_COLORS:
        return NAMED_COLORS[key]
    if value.startswith("#") and len(value) == 7:
        return (
            int(value[1:3], 16),
            int(value[3:5], 16),
            int(value[5:7], 16),
        )
    return (0, 0, 0)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


class DrawingApp:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        pygame.display.set_caption("Drawing App")
        self.clock = pygame.time.Clock()
        self.canvas = pygame.Surface((WINDOW_W, CANVAS_H))
        self.canvas.fill((255, 255, 255))

        self.palette = [parse_color(c) for c in COLORS]
        self.color_index = 0
        self.brush_size = MIN_BRUSH
        self.eraser_mode = False
        self.drawing = False
        self.last_pos: tuple[int, int] | None = None

        self.font = pygame.font.SysFont("consolas", 16)
        self.font_small = pygame.font.SysFont("consolas", 14)
        self.font_title = pygame.font.SysFont("consolas", 15, bold=True)

    @property
    def current_color(self) -> tuple[int, int, int]:
        if self.eraser_mode:
            return (255, 255, 255)
        return self.palette[self.color_index]

    def cycle_color(self) -> None:
        self.eraser_mode = False
        self.color_index = (self.color_index + 1) % len(self.palette)

    def cycle_brush_size(self) -> None:
        if self.brush_size >= MAX_BRUSH:
            self.brush_size = MIN_BRUSH
        else:
            self.brush_size += 1

    def set_eraser(self) -> None:
        self.eraser_mode = True

    def draw_stroke(self, pos: tuple[int, int]) -> None:
        color = self.current_color
        if self.last_pos is not None:
            pygame.draw.line(
                self.canvas,
                color,
                self.last_pos,
                pos,
                self.brush_size,
            )
        pygame.draw.circle(
            self.canvas,
            color,
            pos,
            max(1, self.brush_size // 2),
        )
        self.last_pos = pos

    def handle_click(self, pos: tuple[int, int], button: int) -> None:
        if button != 1:
            return
        if ERASER_BTN.collidepoint(pos):
            self.set_eraser()
            return
        if pos[1] < CANVAS_H:
            self.drawing = True
            self.last_pos = None
            self.draw_stroke(pos)

    def draw_ui(self) -> None:
        # Bottom bar
        pygame.draw.rect(self.screen, (240, 240, 240), (0, CANVAS_H, WINDOW_W, 60))
        pygame.draw.line(self.screen, (180, 180, 180), (0, CANVAS_H), (WINDOW_W, CANVAS_H), 2)

        # Eraser button
        btn_color = (200, 80, 80) if self.eraser_mode else (220, 220, 220)
        pygame.draw.rect(self.screen, btn_color, ERASER_BTN, border_radius=6)
        pygame.draw.rect(self.screen, (100, 100, 100), ERASER_BTN, 2, border_radius=6)
        label = self.font.render("Eraser", True, (30, 30, 30))
        self.screen.blit(
            label,
            label.get_rect(center=ERASER_BTN.center),
        )

        # Current tool info (left of eraser area)
        mode = "ERASER" if self.eraser_mode else "BRUSH"
        col = self.current_color
        info = self.font.render(
            f"{mode}  size {self.brush_size}  {rgb_to_hex(col)}",
            True,
            (40, 40, 40),
        )
        self.screen.blit(info, (160, CANVAS_H + 18))

        # Color swatch
        swatch = pygame.Rect(WINDOW_W - 200, CANVAS_H + 12, 36, 36)
        pygame.draw.rect(self.screen, col, swatch)
        pygame.draw.rect(self.screen, (80, 80, 80), swatch, 2)

        # Instructions — top right
        panel_w = 260
        panel_h = 20 + len(INSTRUCTIONS) * 22
        panel_x = WINDOW_W - panel_w - 12
        panel_y = 12
        panel = pygame.Rect(panel_x, panel_y, panel_w, panel_h)
        overlay = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 210))
        self.screen.blit(overlay, panel.topleft)
        pygame.draw.rect(self.screen, (120, 120, 120), panel, 1)

        title = self.font_title.render("How to use", True, (20, 20, 20))
        self.screen.blit(title, (panel_x + 10, panel_y + 8))
        for i, line in enumerate(INSTRUCTIONS):
            text = self.font_small.render(line, True, (40, 40, 40))
            self.screen.blit(text, (panel_x + 10, panel_y + 32 + i * 22))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.cycle_color()
                    elif event.key in (pygame.K_1, pygame.K_KP1):
                        self.cycle_brush_size()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos, event.button)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.drawing = False
                        self.last_pos = None

                elif event.type == pygame.MOUSEMOTION:
                    if self.drawing and event.pos[1] < CANVAS_H:
                        self.draw_stroke(event.pos)

            self.screen.blit(self.canvas, (0, 0))
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(60)


def main() -> None:
    app = DrawingApp()
    app.run()


if __name__ == "__main__":
    main()