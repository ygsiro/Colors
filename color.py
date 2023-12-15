class RGB:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self.red = self.__clamp(red, 0, 255)
        self.green = self.__clamp(green, 0, 255)
        self.blue = self.__clamp(blue, 0, 255)

    def __clamp(self, val, min_v, max_v):
        if val <= min_v:
            return min_v
        elif val >= max_v:
            return max_v
        else:
            return val

    def hex(self) -> str:
        return (
            f"#{format(self.red, 'x')}{format(self.green, 'x')}{format(self.blue, 'x')}"
        )

    def rel_lum(self) -> float:
        def calc(color):
            color /= 255
            if color <= 0.03928:
                return color / 12.92
            else:
                return ((color + 0.055) / 1.055) ** 2.4

        R = calc(self.red)
        G = calc(self.green)
        B = calc(self.blue)
        return 0.2126 * R + 0.7152 * G + 0.0722 * B

    def __str__(self) -> str:
        return f"rgb({self.red}, {self.green}, {self.blue})"


def contrast_ratio(color1: RGB, color2: RGB) -> float:
    L1 = color1.rel_lum()
    L2 = color2.rel_lum()
    if L1 > L2:
        return (L1 + 0.05) / (L2 + 0.05)
    else:
        return (L2 + 0.05) / (L1 + 0.05)


color = RGB(128, 128, 128)
print(color)
