# turtle_math_toolkit.py
# Interactive Math & Engineering Visual Toolkit using turtle
# Features:
#  - Axes + grid with pan/zoom
#  - Plot preset functions (switch with F key)
#  - Numerical derivative at mouse click (press 'd')
#  - Numerical definite integral between two clicks (press 'i' after two clicks)
#  - Newton-Raphson root finder starting from a clicked x (press 'n')
#  - Toggle grid (g), clear (c), save EPS (s)
#  - Pan: arrow keys, Zoom: + / -
#
# Designed to be useful for quick visual experiments in calculus, mechanics, signals, etc.
# Only uses Python stdlib (turtle, math).

import turtle as t
import math
import time

# ----- Configuration -----
WIDTH, HEIGHT = 1000, 700
GRID_SPACING = 50  # pixels for grid step at scale=1
AXIS_COLOR = "black"
GRID_COLOR = "#e6e6e6"
FUNC_COLORS = ["red", "blue", "green", "purple", "orange", "brown"]

# ----- Camera / View state -----
cam_x, cam_y = 0.0, 0.0  # world coords at screen center
scale = 1.0             # pixels per unit (multiplied by GRID_SPACING)

# ----- Interaction state -----
click_points = []  # store x positions for integration/root-finding
show_grid = True

# ----- Preset functions (label, lambda) -----
# Use math.* functions only
safe_math = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
safe_math.update({"abs": abs, "pow": pow})

functions = [
    ("y = sin(x)", lambda x: math.sin(x)),
    ("y = cos(x)", lambda x: math.cos(x)),
    ("y = x**2", lambda x: x**2),
    ("y = 0.1*x**3 - 0.5*x", lambda x: 0.1*x**3 - 0.5*x),
    ("y = exp(-0.2*x)*cos(2*x)", lambda x: math.exp(-0.2*x)*math.cos(2*x)),
    ("y = 1/(1+x**2)", lambda x: 1/(1+x**2)),
]

current_func = 0

# ----- Turtle setup -----
screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Math Toolkit - Turtle")
screen.tracer(0, 0)
drawer = t.Turtle(visible=False)
drawer.speed(0)
drawer.penup()

# Coordinate helpers (world <-> screen)
def world_to_screen(wx, wy):
    sx = (wx - cam_x) * (GRID_SPACING * scale) + WIDTH/2
    sy = (wy - cam_y) * (GRID_SPACING * scale) + HEIGHT/2
    return sx - WIDTH/2, sy - HEIGHT/2  # turtle's coordinates centered at 0,0

def screen_to_world(sx, sy):
    wx = cam_x + sx / (GRID_SPACING * scale)
    wy = cam_y + sy / (GRID_SPACING * scale)
    return wx, wy

# Draw grid and axes
def draw_grid():
    drawer.clear()
    if show_grid:
        drawer.pencolor(GRID_COLOR)
        drawer.pensize(1)
        step = GRID_SPACING * scale
        # vertical lines
        x = -WIDTH/2 - (cam_x*(GRID_SPACING*scale)%step)
        n = int(WIDTH/step) + 4
        for i in range(n):
            drawer.penup()
            drawer.goto(x + i*step, -HEIGHT/2)
            drawer.pendown()
            drawer.goto(x + i*step, HEIGHT/2)
        # horizontal lines
        y = -HEIGHT/2 - (cam_y*(GRID_SPACING*scale)%step)
        m = int(HEIGHT/step) + 4
        for j in range(m):
            drawer.penup()
            drawer.goto(-WIDTH/2, y + j*step)
            drawer.pendown()
            drawer.goto(WIDTH/2, y + j*step)
    # axes
    drawer.pencolor(AXIS_COLOR)
    drawer.pensize(2)
    # y axis
    sx, _ = world_to_screen(0,0)
    drawer.penup(); drawer.goto(sx, -HEIGHT/2); drawer.pendown(); drawer.goto(sx, HEIGHT/2)
    # x axis
    _, sy = world_to_screen(0,0)
    drawer.penup(); drawer.goto(-WIDTH/2, sy); drawer.pendown(); drawer.goto(WIDTH/2, sy)

# Plot function
def plot_current_function():
    label, f = functions[current_func]
    drawer.pencolor(FUNC_COLORS[current_func % len(FUNC_COLORS)])
    drawer.pensize(2)
    # sample density depends on scale
    pixels = WIDTH
    step_px = 1
    first = True
    for sx in range(-WIDTH//2, WIDTH//2+1, step_px):
        wx, wy = screen_to_world(sx, 0)
        try:
            y = f(wx)
            sy = (y - cam_y) * (GRID_SPACING * scale)
            drawer.goto(sx, sy)
            if first:
                drawer.pendown(); first = False
            else:
                drawer.pendown()
        except Exception:
            drawer.penup()
            first = True
    # label
    drawer.penup()
    drawer.goto(-WIDTH/2+10, HEIGHT/2-30)
    drawer.pencolor("black")
    drawer.write(f"Function: {label}  (scale={scale:.2f})", font=("Arial", 12, "normal"))

# Numerical derivative (central difference)
def numerical_derivative(f, x, h=1e-5):
    try:
        return (f(x+h) - f(x-h)) / (2*h)
    except Exception:
        return None

# Numerical integration (trapezoid)
def numerical_integral(f, a, b, n=1000):
    if a == b: return 0.0
    if b < a:
        return -numerical_integral(f, b, a, n)
    h = (b - a) / n
    total = 0.5 * (safe_eval_f(f, a) + safe_eval_f(f, b))
    for i in range(1, n):
        total += safe_eval_f(f, a + i*h)
    return total * h

# Newton-Raphson for root finding (uses numerical derivative)
def newton_root(f, x0, max_iter=50, tol=1e-8):
    x = x0
    for i in range(max_iter):
        fx = safe_eval_f(f, x)
        dfx = numerical_derivative(lambda z: safe_eval_f(f, z), x)
        if dfx is None or abs(dfx) < 1e-12:
            return None, i
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return None, max_iter

# Safe eval wrapper for f(x) - accepts either a python callable or a string expression
def safe_eval_f(f, x):
    if callable(f):
        return f(x)
    else:
        # expression string: evaluate using safe_math
        try:
            return eval(f, {"__builtins__": {}}, dict(safe_math, x=x))
        except Exception as e:
            raise

# Interaction callbacks
def redraw_all():
    screen.tracer(0,0)
    draw_grid()
    plot_current_function()
    screen.update()

def zoom_in():
    global scale
    scale *= 1.2
    redraw_all()

def zoom_out():
    global scale
    scale /= 1.2
    redraw_all()

def pan_left():
    global cam_x; cam_x -= 0.5/scale; redraw_all()

def pan_right():
    global cam_x; cam_x += 0.5/scale; redraw_all()

def pan_up():
    global cam_y; cam_y += 0.5/scale; redraw_all()

def pan_down():
    global cam_y; cam_y -= 0.5/scale; redraw_all()

def toggle_grid():
    global show_grid; show_grid = not show_grid; redraw_all()

def clear_marks():
    global click_points
    click_points = []
    redraw_all()

def save_eps():
    try:
        cv = screen.getcanvas()
        cv.postscript(file="math_plot.eps")
        print("Saved math_plot.eps")
    except Exception as e:
        print("Save failed:", e)

def switch_function():
    global current_func
    current_func = (current_func + 1) % len(functions)
    redraw_all()

def on_click(x, y):
    # Convert screen x,y to world x
    wx, wy = screen_to_world(x, y)
    click_points.append(wx)
    # mark point
    drawer.penup()
    sx, sy = world_to_screen(wx, wy)
    drawer.goto(sx, sy)
    drawer.dot(6, "black")
    screen.update()

def do_derivative_at_click():
    # Use last click point
    if not click_points:
        print("Click somewhere first (mouse).")
        return
    x = click_points[-1]
    f = functions[current_func][1]
    d = numerical_derivative(lambda z: safe_eval_f(f, z), x, h=1e-6)
    if d is None:
        print("Could not compute derivative at x =", x)
        return
    print(f"f'({x:.6g}) ≈ {d:.6g}")
    # draw tangent line segment
    drawer.pencolor("black"); drawer.pensize(1)
    L = 2.0  # length in world units each side
    x1, x2 = x - L, x + L
    y1 = safe_eval_f(f, x1); y2 = safe_eval_f(f, x2)
    sx1, sy1 = world_to_screen(x1, y1)
    sx2, sy2 = world_to_screen(x2, y2)
    drawer.penup(); drawer.goto(sx1, sy1); drawer.pendown(); drawer.goto(sx2, sy2)
    screen.update()

def do_integral_between_clicks():
    if len(click_points) < 2:
        print("Need two clicks (two x positions). Click twice and then press 'i'.")
        return
    a, b = click_points[-2], click_points[-1]
    f = functions[current_func][1]
    try:
        val = numerical_integral(f, a, b, n=2000)
        print(f"∫ f(x) dx from {a:.6g} to {b:.6g} ≈ {val:.6g}")
        # shade area (simple polygon)
        nx = 200
        xs = [a + (b-a)*i/nx for i in range(nx+1)]
        points = []
        for xx in xs:
            yy = safe_eval_f(f, xx)
            sx, sy = world_to_screen(xx, yy)
            points.append((sx, sy))
        # draw polygon
        drawer.fillcolor((0.5,0.5,0.9))
        drawer.penup()
        drawer.goto(points[0])
        drawer.begin_fill()
        for px, py in points:
            drawer.goto(px, py)
        # close along x-axis (world y=0)
        sx_a, sy_a = world_to_screen(b, 0)
        sx_b, sy_b = world_to_screen(a, 0)
        drawer.goto(sx_a, sy_a)
        drawer.goto(sx_b, sy_b)
        drawer.end_fill()
        screen.update()
    except Exception as e:
        print("Integral failed:", e)

def do_newton_from_click():
    if not click_points:
        print("Click an x to start Newton method.")
        return
    x0 = click_points[-1]
    f = functions[current_func][1]
    root, iters = newton_root(f, x0, max_iter=80)
    if root is None:
        print("Newton failed to converge from x0 =", x0)
    else:
        print(f"Newton root ≈ {root:.6g} (iterations: {iters})")
        # mark root
        sx, sy = world_to_screen(root, 0)
        drawer.penup(); drawer.goto(sx, sy); drawer.dot(8, "red")
        screen.update()

# Keyboard bindings
screen.onclick(on_click)
screen.listen()
screen.onkey(zoom_in, "+")
screen.onkey(zoom_out, "-")
screen.onkey(pan_left, "Left")
screen.onkey(pan_right, "Right")
screen.onkey(pan_up, "Up")
screen.onkey(pan_down, "Down")
screen.onkey(toggle_grid, "g")
screen.onkey(clear_marks, "c")
screen.onkey(save_eps, "s")
screen.onkey(switch_function, "f")
screen.onkey(do_derivative_at_click, "d")
screen.onkey(do_integral_between_clicks, "i")
screen.onkey(do_newton_from_click, "n")

# Initial draw
redraw_all()

# Instruction print
print("""Math Toolkit - instruções rápidas:
 - Clique com o mouse para adicionar pontos (essas coordenadas X são usadas para 'd', 'i', 'n').
 - 'f' : alterna função plotada (predefinidas).
 - '+' / '-' : zoom in/out.
 - Setas : pan (mover a vista).
 - 'd' : calcula e mostra derivada numérica no último X clicado (desenha tangente).
 - 'i' : calcula integral numérica entre os dois últimos X clicados e sombreia a área.
 - 'n' : aplica Newton-Raphson a partir do último X clicado e marca a raiz encontrada.
 - 'g' : alterna grid.
 - 'c' : limpa marcas (não altera a função).
 - 's' : salva um EPS (math_plot.eps).
""")

t.mainloop()
