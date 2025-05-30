

import reflex as rx

def navbar():
    return rx.hstack(
        rx.text("Portals", color="white", font_weight="bold", font_size="5"),
        rx.spacer(),
        rx.hstack(
            rx.text("Home", color="white"),
            rx.text("Products", color="white"),
            rx.text("Developers", color="white"),
            rx.text("Contact", color="white"),
            spacing="8",
        ),
        rx.spacer(),
        rx.button(
            "Book a demo",
            background_color="#6f2db6",
            color="white",
            border_radius="8px",
            padding_x="4",
            padding_y="2",
        ),
        padding="6",
        background_color="black",
        width="100%",
        align_items="center"
    )

def hero_section():
    return rx.center(
        rx.vstack(
            rx.heading("Unleash your creativity", color="white", font_size="9", font_weight="bold"),
            rx.text(
                "Design, share, and express your ideas freely with our tools.",
                color="white",
                font_size="5",
                max_width="30em",
                text_align="center"
            ),
            rx.button(
                "Get Started",
                background_color="white",
                color="black",
                border_radius="999px",
                padding_x="6",
                padding_y="4"
            ),
            spacing="6",
            align_items="center"
        ),
        padding_y="16",
        position="absolute",
        top=0,
        left=0,
        right=0,
        z_index="1"
    )

def index():
    return rx.box(
        rx.image(
            src="/fondeo.png",
            position="absolute",
            width="100%",
            height="100%",
            object_fit="cover",
            z_index="0"
        ),
        rx.box(
            navbar(),
            hero_section(),
            position="relative",
            z_index="1",
        ),
        width="100%",
        height="100vh",
        overflow="hidden",
        position="relative"
    )

app = rx.App()
app.add_page(index, title="Creative Landing Page")
