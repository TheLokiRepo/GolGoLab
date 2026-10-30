"""Exporta el esquema de GolGoLab a PNG y SVG; requiere Pillow."""

from pathlib import Path
from html import escape
import math

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W, H, SCALE = 2100, 1690, 2
im = Image.new("RGB", (W * SCALE, H * SCALE), "#F5F7FB")
draw = ImageDraw.Draw(im)
FONT = Path("/usr/share/fonts/truetype/dejavu")
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<title>Ecosistema de GolGoLab</title>',
       '<desc>Frontal Angular, tres servicios iniciales, persistencia, Garmin y evolución hacia IA, asistente, Android y MCP.</desc>',
       f'<rect width="{W}" height="{H}" fill="#F5F7FB"/>']


def text(x, y, value, size=25, color="#192C40", bold=False, anchor="start"):
    font = ImageFont.truetype(str(FONT / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")), size * SCALE)
    draw.text((x * SCALE, y * SCALE), value, font=font, fill=color,
              anchor={"start": "lm", "middle": "mm", "end": "rm"}[anchor])
    svg.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{size}" '
               f'font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}" '
               f'dominant-baseline="central">{escape(value)}</text>')


def stroke(points, color="#58778F", width=3, dashed=False):
    pts = [(x * SCALE, y * SCALE) for x, y in points]
    if dashed:
        for a, b in zip(pts, pts[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            length = math.hypot(dx, dy)
            if not length:
                continue
            for t in range(0, math.ceil(length), 20 * SCALE):
                end = min(t + 11 * SCALE, length)
                draw.line([(a[0] + dx * t / length, a[1] + dy * t / length),
                           (a[0] + dx * end / length, a[1] + dy * end / length)],
                          fill=color, width=width * SCALE)
    else:
        draw.line(pts, fill=color, width=width * SCALE, joint="curve")
    dash = ' stroke-dasharray="11 9"' if dashed else ""
    coords = " ".join(f"{x},{y}" for x, y in points)
    svg.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}" '
               f'stroke-linejoin="round"{dash}/>')


def arrow(points, future=False, both=False):
    color = "#9673B9" if future else "#58778F"
    stroke(points, color=color, dashed=future)
    ends = [(points[-2], points[-1])]
    if both:
        ends.append((points[1], points[0]))
    for a, b in ends:
        angle = math.atan2(b[1] - a[1], b[0] - a[0])
        triangle = [b, (b[0] - 13 * math.cos(angle) + 6 * math.sin(angle),
                        b[1] - 13 * math.sin(angle) - 6 * math.cos(angle)),
                       (b[0] - 13 * math.cos(angle) - 6 * math.sin(angle),
                        b[1] - 13 * math.sin(angle) + 6 * math.cos(angle))]
        draw.polygon([(x * SCALE, y * SCALE) for x, y in triangle], fill=color)
        svg.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in triangle)}" fill="{color}"/>')


def rect(x, y, w, h, fill="#FFFFFF", border="#D6E0EA", radius=16, dashed=False):
    draw.rounded_rectangle((x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE),
                           radius=radius * SCALE, fill=fill,
                           outline=None if dashed else border, width=2 * SCALE)
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
               f'fill="{fill}" stroke="{border}" stroke-width="2"{dash}/>')
    if dashed:
        # El borde discontinuo del PNG sigue el mismo contorno lógico que el SVG.
        for pts in [[(x + radius, y), (x + w - radius, y)],
                    [(x + w, y + radius), (x + w, y + h - radius)],
                    [(x + radius, y + h), (x + w - radius, y + h)],
                    [(x, y + radius), (x, y + h - radius)]]:
            # La forma vectorial ya incluye el borde; dibujar aquí solo el PNG.
            saved = len(svg)
            stroke(pts, color=border, width=2, dashed=True)
            del svg[saved:]


def group(x, y, w, h, title, subtitle=None, purple=False):
    rect(x, y, w, h, fill="#F5F0FA" if purple else "#EAF0F6",
         border="#D9CBE8" if purple else "#D4DFE9", radius=22)
    text(x + 28, y + 31, title, 23, "#6C488A" if purple else "#47627C", bold=True)
    if subtitle:
        text(x + 28, y + 59, subtitle, 19, "#64788A")


def box(x, y, w, h, title, lines, future=False, external=False):
    rect(x, y, w, h, fill="#FBF7FF" if future else ("#F0FAF6" if external else "#FFFFFF"),
         border="#9673B9" if future else ("#6BA18A" if external else "#8DA7BD"),
         dashed=future)
    text(x + 22, y + 31, title, 25, "#704C90" if future else "#18364F", bold=True)
    for index, line in enumerate(lines):
        text(x + 22, y + 67 + index * 29, line, 22, "#4A5F73")


text(50, 56, "GolGoLab", 45, bold=True)
text(50, 103, "Ecosistema previsto · inicio local · cuentas separadas", 25, "#596E83")
rect(1220, 35, 25, 25, fill="#FFFFFF", border="#8DA7BD", radius=5)
text(1258, 48, "Primera entrega", 22)
rect(1540, 35, 25, 25, fill="#FBF7FF", border="#9673B9", radius=5, dashed=True)
text(1578, 48, "Posterior / futuro", 22)
text(2050, 96, "Diseño funcional · tecnologías aún por cerrar", 19, "#64788A", anchor="end")

group(300, 150, 1350, 220, "INTERFAZ")
group(50, 405, 1600, 455, "BACKEND · EJECUCIÓN LOCAL", "Tres servicios independientes; IA en una entrega posterior")
group(50, 915, 1600, 240, "PERSISTENCIA", "Motor pendiente")
group(50, 1195, 1600, 160, "OPERACIÓN · FUNCIONES TRANSVERSALES", "Diseño pendiente; no son microservicios adicionales")
group(50, 1400, 1600, 195, "POSIBILIDADES FUTURAS", purple=True)
text(1730, 413, "EXTERNOS", 22, "#47627C", bold=True)

# Conexiones, antes de las cajas para que las puntas lleguen a sus bordes.
arrow([(270, 265), (330, 265)])
arrow([(695, 325), (695, 385), (840, 385), (840, 455)])
arrow([(1060, 300), (1120, 300)], future=True)
arrow([(1360, 325), (1360, 385), (1055, 385), (1055, 505), (1030, 505)], future=True)
arrow([(840, 560), (840, 605), (310, 605), (310, 650)])
arrow([(840, 560), (840, 605), (875, 605), (875, 650)])
arrow([(1030, 540), (1085, 540), (1085, 605), (1370, 605), (1370, 650)], future=True)
arrow([(1100, 700), (1125, 700), (1125, 510), (1730, 510)], both=True)
arrow([(1580, 715), (1730, 715)], future=True)
arrow([(310, 785), (310, 1000)])
arrow([(875, 785), (875, 1000)])
arrow([(1370, 785), (1370, 1000)], future=True)
arrow([(695, 210), (695, 133), (1890, 133), (1890, 450)])
text(1240, 118, "Autorizar en Garmin desde el frontal", 20, "#58778F", anchor="middle")
text(1380, 493, "Autorización y datos", 20, "#58778F", anchor="middle")

box(60, 215, 210, 100, "Usuario", ["Cuenta propia"])
box(330, 210, 730, 115, "Frontal Angular", ["Dashboard, gráficos, histórico e hitos", "Gestión de usuarios y botón «Vincular Garmin»"])
box(1120, 210, 480, 115, "Asistente persistente", ["Consultas y posible navegación", "Reparto 70/30 por madurar"], future=True)
box(650, 455, 380, 105, "API y orquestación", ["Entrada y coordinación"])
box(120, 650, 380, 135, "Servicio de usuarios", ["Cuentas y perfiles", "Autenticación y permisos"])
box(650, 650, 450, 135, "Garmin y datos deportivos", ["Vinculación y sincronización", "Consultas por día y por rango"])
box(1160, 650, 420, 135, "Servicio de IA", ["Prompts, contexto y análisis", "Entrega posterior"], future=True)
box(1730, 450, 320, 155, "Garmin Connect", ["Autorización oficial", "y APIs de datos", "Acceso por validar"], external=True)
box(1730, 650, 320, 135, "API de OpenAI", ["Acceso y consumo", "propios del usuario"], future=True)

box(120, 1000, 380, 125, "Datos de usuarios", ["Identidad, perfiles y permisos"])
box(650, 1000, 450, 125, "Datos deportivos y conexión", ["Entrenamientos, VFC y sueño", "Histórico y vinculación Garmin"])
box(1160, 1000, 420, 125, "Datos de IA", ["Contexto, memoria y análisis", "Conexión OpenAI"], future=True)
text(80, 1141, "Conjuntos lógicos propuestos; no implican motores ni instancias independientes.", 17, "#64788A")
text(1730, 980, "VINCULACIÓN GARMIN", 22, "#47627C", bold=True)
for idx, line in enumerate(["Sin copiar claves.", "Autorización guardada.", "Renovación si se admite.", "Revincular si deja de ser válida."]):
    text(1730, 1025 + idx * 33, line, 20, "#596E83")

for x, label in [(90, "Secretos protegidos"), (470, "Configuración"), (850, "Registros y trazas"), (1230, "Copias y restauración")]:
    rect(x, 1280, 350, 46, fill="#FFFFFF", border="#D4DFE9", radius=9)
    text(x + 175, 1303, label, 22, anchor="middle")

box(120, 1455, 580, 105, "Aplicación Android", ["Reutiliza Angular · Capacitor por validar"], future=True)
box(900, 1455, 680, 105, "Servidor MCP", ["Clientes ChatGPT / MCP → servidor → API propia"], future=True)
text(50, 1643, "Pendiente principal: validar autorización oficial e histórico de Garmin. Backend .NET / ASP.NET Core propuesto.", 22, "#526C83")
text(2050, 1643, "30 oct 2026", 20, "#7A8C9E", anchor="end")

svg.append("</svg>")
im.save(OUT / "ecosistema.png", optimize=True, dpi=(192, 192))
(OUT / "ecosistema.svg").write_text("\n".join(svg), encoding="utf-8")
print(f"PNG: {im.width} × {im.height} px; SVG: {W} × {H} unidades")
