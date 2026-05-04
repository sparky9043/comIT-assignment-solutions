import datetime
from django.core.management.base import BaseCommand
from menu.models import Location, Chef, MenuItem


class Command(BaseCommand):
    help = "Seeds the database with locations, chefs, and menu items."

    def handle(self, *args, **options):

        # ── Locations ──────────────────────────────────────────────────────

        vancouver = Location.objects.create(
            name="Ember & Oak",
            city="Vancouver",
            open_date=datetime.date(2014, 4, 22),
        )
        calgary = Location.objects.create(
            name="Prairie Table",
            city="Calgary",
            open_date=datetime.date(2017, 8, 10),
        )
        toronto = Location.objects.create(
            name="Harbour & Grain",
            city="Toronto",
            open_date=datetime.date(2012, 3, 5),
        )
        halifax = Location.objects.create(
            name="Salt & Tide",
            city="Halifax",
            open_date=datetime.date(2021, 6, 18),
        )

        self.stdout.write("  Locations created.")

        # ── Chefs ──────────────────────────────────────────────────────────
        # Vancouver: 3 chefs | Calgary: 2 chefs | Toronto: 3 chefs | Halifax: 2 chefs

        c1 = Chef.objects.create(
            first_name="Mei-Ling",
            last_name="Tran",
            dob=datetime.date(1990, 3, 14),
            location=vancouver,
        )
        c2 = Chef.objects.create(
            first_name="Samuel",
            last_name="Oduya",
            dob=datetime.date(1987, 11, 2),
            location=vancouver,
        )
        c3 = Chef.objects.create(
            first_name="Priya",
            last_name="Nair",
            dob=datetime.date(1995, 7, 30),
            location=vancouver,
        )
        c4 = Chef.objects.create(
            first_name="Andrei",
            last_name="Popescu",
            dob=datetime.date(1992, 1, 19),
            location=calgary,
        )
        c5 = Chef.objects.create(
            first_name="Fatima",
            last_name="Al-Rashidi",
            dob=datetime.date(1998, 5, 8),
            location=calgary,
        )
        c6 = Chef.objects.create(
            first_name="James",
            last_name="Okafor",
            dob=datetime.date(1984, 9, 25),
            location=toronto,
        )
        c7 = Chef.objects.create(
            first_name="Yuna",
            last_name="Kim",
            dob=datetime.date(1996, 12, 3),
            location=toronto,
        )
        c8 = Chef.objects.create(
            first_name="Mateus",
            last_name="Ferreira",
            dob=datetime.date(1991, 4, 17),
            location=toronto,
        )
        c9 = Chef.objects.create(
            first_name="Ingrid",
            last_name="Svensson",
            dob=datetime.date(1989, 2, 28),
            location=halifax,
        )
        c10 = Chef.objects.create(
            first_name="Tariq",
            last_name="Hassan",
            dob=datetime.date(1993, 10, 11),
            location=halifax,
        )

        self.stdout.write("  Chefs created.")

        # ── Menu Items ─────────────────────────────────────────────────────
        # Helper to create an item and set its locations in one call

        all_locations = [vancouver, calgary, toronto, halifax]

        def make_item(name, price, course, chef, locations):
            item = MenuItem.objects.create(
                name=name,
                price=price,
                course=course,
                chef=chef,
            )
            item.locations.set(locations)
            return item

        # ── 15 items available at ALL locations ────────────────────────────

        make_item("Roasted Garlic Hummus", 8.50, "appetizer", c1, all_locations)
        make_item("Crispy Calamari", 13.00, "appetizer", c2, all_locations)
        make_item("Tomato Bisque", 9.75, "appetizer", c6, all_locations)
        make_item("Caesar Salad", 11.50, "appetizer", c7, all_locations)
        make_item("Grilled Atlantic Salmon", 28.00, "entree", c3, all_locations)
        make_item("Braised Short Rib", 34.50, "entree", c4, all_locations)
        make_item("Wild Mushroom Risotto", 24.00, "entree", c5, all_locations)
        make_item("Roasted Half Chicken", 26.75, "entree", c6, all_locations)
        make_item("Pan-Seared Halibut", 32.00, "entree", c8, all_locations)
        make_item("Classic Beef Burger", 19.50, "entree", c9, all_locations)
        make_item("Dark Chocolate Lava Cake", 10.00, "dessert", c10, all_locations)
        make_item("Crème Brûlée", 9.50, "dessert", c1, all_locations)
        make_item("House Lemonade", 5.00, "drink", c2, all_locations)
        make_item("Sparkling Water", 3.50, "drink", c3, all_locations)
        make_item("Cold Brew Coffee", 6.25, "drink", c4, all_locations)

        # ── 15 items available at 1–3 locations ───────────────────────────

        # Vancouver only
        make_item("Dungeness Crab Cakes", 17.50, "appetizer", c1, [vancouver])
        make_item("Miso Black Cod", 38.00, "entree", c2, [vancouver])
        make_item("Matcha Panna Cotta", 9.00, "dessert", c3, [vancouver])

        # Calgary only
        make_item("Bison Tartare", 16.00, "appetizer", c4, [calgary])
        make_item("Alberta Dry-Aged Ribeye", 52.00, "entree", c5, [calgary])

        # Toronto only
        make_item("Peking Duck Spring Rolls", 14.50, "appetizer", c6, [toronto])
        make_item("Jerk Chicken Flatbread", 22.00, "entree", c7, [toronto])
        make_item("Butter Tart", 7.50, "dessert", c8, [toronto])

        # Halifax only
        make_item("Digby Scallop Ceviche", 15.00, "appetizer", c9, [halifax])
        make_item("Lobster Tagliatelle", 42.00, "entree", c10, [halifax])

        # Vancouver + Calgary
        make_item("Elk Carpaccio", 18.00, "appetizer", c1, [vancouver, calgary])
        make_item("Truffle Fries", 11.00, "appetizer", c4, [vancouver, calgary])

        # Toronto + Halifax
        make_item("Smoked Salmon Blini", 13.50, "appetizer", c9, [toronto, halifax])
        make_item("Maple Crème Caramel", 8.75, "dessert", c10, [toronto, halifax])

        # Vancouver + Toronto + Halifax
        make_item("Yuzu Gin & Tonic", 14.00, "drink", c3, [vancouver, toronto, halifax])

        self.stdout.write("  Menu items created.")
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
