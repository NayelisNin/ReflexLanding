

import reflex as rx

def navbar():
    
    return rx.hstack(
        rx.vstack(
        rx.spacer(),
        rx.text("*connect", font_size="1em"),
        rx.color_mode.button(position="top-right"),
        ),


        rx.hstack(
           rx.spacer(),
           rx.spacer(),
           rx.spacer(),
           rx.spacer(),
           rx.spacer(),
           rx.spacer(),
           rx.spacer(),
            rx.text("Solutions"),
            rx.text("Partnership"),
            rx.text("Pricing"),
            rx.text("Contact"),
            spacing="9",
            align="center",
            
        ),

    ),
        
       
        

def hero_section():
    return rx.center(
        rx.vstack(
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.heading("Unleash your creativity whith plattaform", font_size="9", font_weight="bold", align="center", marging_left="5em"),
            rx.text(
                "Design, share, and express your ideas freely with our tools, you can create unique content than can be edited and modified. A fun and engaging experience for you and your audience.",
                font_size="5",
                max_width="30em",
                text_align="center"
            ),
            rx.button(
                "Get Started",

                border_radius="999px",
                bg="green",
                padding_x="6",
                padding_y="4"
            ),
            spacing="6",
            align_items="center"
        ),
        padding_y="16",
        position="absolute",
        top=7,
        left=0,
        right=0,
        z_index="1"
    )



    

def index():
    return rx.box(
        
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
