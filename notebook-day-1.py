import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return la, np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell
def _():
    g = 1
    M = 1
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le réacteur est situé à la base du booster. L'axe du booster fait un angle $\theta$ avec la verticale. La force $f$ fait un angle $\phi$ avec l'axe du booster.

    Les coordonnées cartésiennes de la force sont :

    $$f_x = -f \sin(\theta + \phi), \qquad f_y = f \cos(\theta + \phi)$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On applique la deuxième loi de Newton $M\ddot{\vec{r}} = \vec{F}$ :

    $$M\ddot{x} = -f\sin(\theta + \phi)$$

    $$M\ddot{y} = f\cos(\theta + \phi) - Mg$$

    ce qui donne :

    $$\ddot{x} = \frac{f}{M}\sin(\theta+\phi), \qquad \ddot{y} = \frac{f}{M}\cos(\theta+\phi) - g$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour une tige homogène de longueur $\ell$ et de masse $M$ tournant autour de son centre :

    $$
    J = \frac{M \ell^2}{12}.
    $$

    Avec $M=1$ et $\ell=2$, on obtient $J = 1/3$.
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 12
    return (J,)


@app.cell
def _(J):
    J
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le réacteur est situé à la base, à la distance $\ell/2$ du centre de masse. Sa position par rapport au centre vaut $(\,\tfrac{\ell}{2}\sin\theta, -\tfrac{\ell}{2}\cos\theta)$. Le couple ($z$-composante) $\tau = r_x F_y - r_y F_x$ vaut :

    $$
    \tau = \frac{\ell f}{2}\big(\sin\theta\cos(\theta+\phi) - \cos\theta\sin(\theta+\phi)\big)
         = -\frac{\ell f}{2}\sin\phi.
    $$

    D'où l'équation de l'inclinaison :

    $$
    J\,\ddot{\theta} = -\frac{\ell\,f}{2}\sin\phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    L'état est de dimension $n = 6$ :

    $$
    s = (x, v_x, y, v_y, \theta, \omega).
    $$

    Le système $\dot{s} = F(s, f, \phi)$ s'écrit

    $$
    F(s, f, \phi) =
    \begin{pmatrix}
    v_x \\
    -f\sin(\theta+\phi)/M \\
    v_y \\
    f\cos(\theta+\phi)/M - g \\
    \omega \\
    -\ell\,f\,\sin\phi/(2J)
    \end{pmatrix}.
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s
        fx = -f * np.sin(theta + phi)
        fy =  f * np.cos(theta + phi)
        return np.array([
            vx,
            fx / M,
            vy,
            fy / M - g,
            omega,
            -l * f * np.sin(phi) / (2 * J),
        ])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, s):
            f, phi = f_phi(t, s)
            return F(s, f, phi)
        result = sci.solve_ivp(
            rhs, t_span, y0, dense_output=True,
            rtol=1e-8, atol=1e-10, max_step=0.05,
        )
        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Avec $y(0)=10$, $\dot y(0)=0$, $f=0$, on a $\ddot y = -g = -1$ donc $y(t) = 10 - t^2/2$. Le centre de masse croise $y = \ell = 2$ pour

    $$
    t = \sqrt{2(10-\ell)} = \sqrt{16} = 4\ \text{s}.
    $$
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0])
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(t, y_t, label=r"$y(t)$ (hauteur en mètres)")
        ax.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        ax.axvline(4.0, color="red", ls=":", label=r"$t = 4$ s (croisement théorique)")
        ax.set_title("Chute libre")
        ax.set_xlabel("temps $t$")
        ax.grid(True)
        ax.legend()
        plt.show()

    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Conditions : $y(0)=10$, $\dot y(0)=-2$, $\theta=\phi=0$, $y(5)=\ell/2=1$, $\dot y(5)=0$.

    On cherche $y(t)$ polynomial cubique vérifiant ces 4 conditions ainsi que $f(t)=M(\ddot y+g)$.
    """)
    return


@app.cell
def _(M, g, l, la, np, plt, redstart_solve):
    A = np.array([
        [1, 0,  0,    0],
        [0, 1,  0,    0],
        [1, 5, 25,  125],
        [0, 1, 10,   75],
    ])
    rhs = np.array([10.0, -2.0, 1.0, 0.0])
    a, b, c, d = la.solve(A, rhs)
    print(f"a={a}, b={b}, c={c}, d={d}")

    def f_landing(t):
        return M * (2 * c + 6 * d * t + g)

    def controlled_landing():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, s):
            return np.array([f_landing(t), 0.0])
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        s = sol(t)

        fig, axes = plt.subplots(2, 1, figsize=(8, 9), sharex=True)

        axes[0].plot(t, s[2], color="tab:blue", lw=2, label=r"$y(t)$ (simulation)")
        axes[0].axhline(l/2, color="green", ls="--", label=r"cible $y=\ell/2=1$")
        axes[0].set_ylabel("hauteur $y$ (m)")
        axes[0].set_title("Hauteur du centre de masse")
        axes[0].grid(True); axes[0].legend(loc="upper right", framealpha=0.9)

        axes[1].plot(t, s[3], color="tab:orange", lw=2, label=r"$\dot y(t)$ (simulation)")
        axes[1].axhline(0, color="green", ls="--", label=r"cible $\dot y=0$")
        axes[1].set_ylabel("vitesse $\\dot y$ (m/s)")
        axes[1].set_title("Vitesse verticale")
        axes[1].grid(True); axes[1].legend(loc="lower right", framealpha=0.9)

        plt.suptitle("Atterrissage contrôlé")
        plt.tight_layout()
        plt.show()

        print(f"y(5)  = {sol(5.0)[2]:.6f}  (cible : 1.0)")
        print(f"vy(5) = {sol(5.0)[3]:.6f}  (cible : 0.0)")

    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(mo, svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        width = x_max - x_min
        height = y_max - y_min
        return svg.svg(
            viewBox=f"0 0 {width} {height}",
            xmlns="http://www.w3.org/2000/svg",
            width="320",
        )(
            transform.translate(x=-x_min, y=y_max)(
                transform.scale(x=1, y=-1)(
                    svg.rect(x=x_min, y=0, width=width, height=y_max,
                             fill="#87CEEB"),                       # ciel
                    svg.rect(x=x_min, y=y_min, width=width, height=-y_min,
                             fill="#8B5A2B"),                       # sol
                    svg.rect(x=-1, y=-0.05, width=2, height=0.1,
                             fill="green"),                          # cible
                    *objects,
                )
            )
        )

    # Test : trois scènes côte à côte
    mo.Html(
        "<div style='display:flex; gap:1em; justify-content:space-around;'>"
        + str(world([-3, 3, -2, 4]))
        + str(world([-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black")))
        + str(world([-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue")))
        + "</div>"
    )
    return (world,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, mo, np, svg, transform, world):
    def booster(x, y, theta, f, phi):
        body_w  = 0.2
        flame_w = 0.25
        flame_len = (l / 2) * (f / (M * g)) if f > 0 else 0.0
        theta_deg = np.degrees(theta)
        phi_deg   = np.degrees(phi)
        return transform.translate(x=x, y=y)(
            transform.rotate(a=theta_deg)(
                svg.rect(
                    x=-body_w/2, y=-l/2, width=body_w, height=l,
                    fill="silver", stroke="black", stroke_width=0.02,
                ),
                transform.translate(x=0, y=-l/2)(
                    transform.rotate(a=phi_deg)(
                        svg.polygon(
                            points=f"{-flame_w/2},0 {flame_w/2},0 0,{-flame_len}",
                            fill="orange", stroke="red", stroke_width=0.02,
                        )
                    )
                )
            )
        )

    mo.Html(
        "<div style='display:flex; gap:1em; justify-content:space-around;'>"
        + str(world([-3, 3, -2, 4], booster(0, l/2, 0, 0, 0)))
        + str(world([-3, 3, -2, 4], booster(0, l, 0, M * g, 0)))
        + str(world([-3, 3, -2, 4],
                    booster(-l/2, l, np.pi/4, 2*M*g, np.pi/2)))
        + "</div>"
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


if __name__ == "__main__":
    app.run()
