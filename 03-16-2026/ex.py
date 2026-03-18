"""
SIMPLE EXERCISE: My Favorite Places Map

A beginner-friendly introduction to OOP with maps!

OBJECTIVES:
1. Learn the 4 pillars of OOP with simple examples
2. Create a map of your favorite places
3. No complex APIs - we'll use simple sample data

WHAT YOU'LL LEARN:
- Encapsulation: Keeping data and methods together
- Abstraction: Hiding complex details
- Inheritance: Creating specialized classes
- Polymorphism: Same method, different behavior

BEFORE YOU BEGIN:
Install required package:
    pip install folium
"""

import folium
import webbrowser
import math

# ============================================================================
# PART 1: BASE CLASS - Learning Encapsulation
# ============================================================================

class Place:
    """
    A simple place with a name and coordinates.
    
    ENCAPSULATION: This class bundles together:
    - Data: name, latitude, longitude
    - Methods: get_info(), distance_to()
    """
    
    def __init__(self, name, latitude, longitude):
        # Attributes (data)
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def get_info(self):
        """Return basic information about this place"""
        return f"{self.name} ({self.latitude}, {self.longitude})"
    
    def distance_to(self, other_place):
        """
        Calculate distance to another place in kilometers
        This is a simplified formula for beginners
        """
        # Difference in latitude and longitude
        lat_diff = self.latitude - other_place.latitude
        lon_diff = self.longitude - other_place.longitude
        
        # Simple Euclidean distance (good enough for learning)
        # 1 degree ≈ 111 km
        distance_km = math.sqrt(lat_diff**2 + lon_diff**2) * 111
        
        return round(distance_km, 2)
    
    def get_marker_color(self):
        """Default marker color - will be overridden by child classes"""
        return "blue"
    
    def get_popup_text(self):
        """Text to show when clicking on marker"""
        return f"<b>{self.name}</b><br>Click for more info!"


# ============================================================================
# PART 2: YOUR TURN! - Practice Inheritance and Polymorphism
# 
# TODO: Create three specialized types of places
# Each should INHERIT from Place and add its own features
# ============================================================================

class Restaurant(Place):
    """
    TODO: Create a Restaurant class that inherits from Place
    
    HINTS:
    1. Use super().__init__() to call the parent constructor
    2. Add a new attribute: food_type (e.g., "Italian", "Chinese")
    3. Override get_popup_text() to show restaurant info
    4. Override get_marker_color() - use "red" for restaurants
    """
    def __init__(self, name, latitude, longitude, food_type):
        super().__init__(name, latitude, longitude)
        self.food_type = food_type
    
    # TODO: Override get_popup_text()
    # Should return: "<b>RESTAURANT: name</b><br>Food: food_type"
    def get_popup_text(self):
        return (f"<b>RESTAURANT: {self.name}</b><br>Food: {self.food_type}")
    
    # TODO: Override get_marker_color()
    # Should return: "red"
    def get_marker_color(self):
        return "red"


class Park(Place):
    """
    TODO: Create a Park class that inherits from Place
    
    HINTS:
    1. Add a new attribute: has_playground (True/False)
    2. Override get_popup_text() to show park info
    3. Override get_marker_color() - use "green" for parks
    """
    
    def __init__(self, name, latitude, longitude, has_playground):
        super().__init__(name, latitude, longitude)
        self.has_playground = has_playground
    # TODO: Override get_popup_text()
    # Should include playground info: "Playground: Yes/No"
    def get_popup_text(self):
        text = "No"
        if self.has_playground:
            text = "Yes"
        return (f"<b>Park: {self.name}</b><br>Playground: {text}")
    
    # TODO: Override get_marker_color()
    # Should return: "green"
    def get_marker_color(self):
        return "green"


class Museum(Place):
    """
    TODO: Create a Museum class that inherits from Place
    
    HINTS:
    1. Add a new attribute: entry_fee (in euros)
    2. Override get_popup_text() to show museum info
    3. Override get_marker_color() - use "purple" for museums
    """
    
    def __init__(self, name, latitude, longitude, entry_fee):
        super().__init__(name, latitude, longitude)
        self.entry_fee = entry_fee
    
    # TODO: Override get_popup_text()
    # Should include: "Entry: €X"
    def get_popup_text(self):
        return (f"<b>Museum: {self.name}</b><br>"
                f"Entry: €{self.entry_fee}")
    
    # TODO: Override get_marker_color()
    # Should return: "purple"
    def get_marker_color(self):
        return "purple"


# ============================================================================
# PART 3: MAP CLASS - More Encapsulation
# ============================================================================

class MyMap:
    """
    This class ENCAPSULATES all map-related functionality
    """
    
    def __init__(self, city, zoom=12):
        """Create a new map centered on a city"""
        self.city = city
        self.places = []  # List to store all our places
        
        # Map centers for some cities
        centers = {
            "Paris": [48.8566, 2.3522],
            "London": [51.5074, -0.1278],
            "New York": [40.7128, -74.0060],
            "Tokyo": [35.6762, 139.6503]
        }
        
        # Get center coordinates or use default
        if city in centers:
            center = centers[city]
        else:
            center = [0, 0]  # Default to (0,0)
            print(f"Warning: {city} not in our list, using (0,0)")
        
        # Create the map
        self.map = folium.Map(location=center, zoom_start=zoom)
        print(f"🗺️  Created map of {city}")
    
    def add_place(self, place):
        """
        Add a place to the map
        
        This demonstrates POLYMORPHISM - the same method works
        for any type of Place (Restaurant, Park, Museum)!
        """
        # Add to our list
        self.places.append(place)
        
        # Create a marker on the map
        folium.Marker(
            location=[place.latitude, place.longitude],
            popup=place.get_popup_text(),  # Different for each place type!
            tooltip=place.name,
            icon=folium.Icon(color=place.get_marker_color())  # Different colors!
        ).add_to(self.map)
        
        print(f"  ✅ Added: {place.name}")
    
    def show_distances(self):
        """
        Show distances between all places
        """
        if len(self.places) < 2:
            print("Add at least 2 places to see distances")
            return
        
        print(f"\n📏 Distances in {self.city}:")
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                place1 = self.places[i]
                place2 = self.places[j]
                dist = place1.distance_to(place2)
                print(f"  {place1.name} → {place2.name}: {dist} km")
    
    def save(self, filename="my_map.html"):
        """Save the map to an HTML file"""
        self.map.save(filename)
        print(f"\n💾 Map saved as '{filename}'")
        return filename


# ============================================================================
# PART 4: CREATE YOUR MAP!
# 
# TODO: Fill in the missing code to create your own map
# ============================================================================

def create_my_places():
    """
    Create a list of your favorite places
    
    TODO: Replace these with your own favorite places!
    """
    places = []
    
    # TODO: Add at least 2 restaurants
    # Example: Restaurant("Pizza Hut", 40.7128, -74.0060, "Italian")
    # restaurants = [...]
    places.append(Restaurant("Chez Janou", 48.85692058124522, 2.3672090253505162, "French"))
    places.append(Restaurant("La Felicita", 48.83525904408256, 2.370202370493764, "Italian"))
    
    # TODO: Add at least 2 parks
    # parks = [...]
    places.append(Park("Franklin Roosevelt Park", 48.93011235468721, 2.2632694025222606, True))
    places.append(Park("Parc Montsouris", 48.83302911244661, 2.3374271144582077, True))
    
    # TODO: Add at least 1 museum
    # museums = [...]
    places.append(Museum("Bourdelle Museum", 48.8444662180575, 2.3190209052448734, 20))
    places.append(Museum("National Museum of Natural History", 48.843675412963904, 2.3552414543617366, 15))
    
    # Combine all places
    # places.extend(restaurants)
    # places.extend(parks)
    # places.extend(museums)
    
    return places


def main():
    """
    Main function - this is where your program starts!
    """
    print("=" * 50)
    print("🗺️  MY FAVORITE PLACES MAP")
    print("=" * 50)
    print("\nThis program demonstrates the 4 pillars of OOP:")
    print("1. ENCAPSULATION: Place class bundles data + methods")
    print("2. INHERITANCE: Restaurant, Park, Museum inherit from Place")
    print("3. POLYMORPHISM: get_popup_text() works differently for each")
    print("4. ABSTRACTION: MyMap hides map complexity")
    print("\n" + "-" * 50)
    
    # TODO 1: Choose a city
    # Available: Paris, London, New York, Tokyo
    my_city = "Paris"  # Change this to your favorite city
    
    # Create a map
    mymap = MyMap(my_city)
    
    # TODO 2: Get your places
    # my_places = create_my_places()
    
    # For now, let's use some sample places (replace with your own!)
    print("\n📝 Using sample places (TODO: Replace with your favorites!)")
    
    # Create some sample places
    eiffel_tower = Place("Eiffel Tower", 48.8584, 2.2945)
    louvre = Museum("Louvre Museum", 48.8606, 2.3376, 17)
    cafe = Restaurant("Cafe Paris", 48.8566, 2.3522, "French")
    park = Park("Luxembourg Garden", 48.8462, 2.3372, True)
    
    # TODO 3: Add all places to the map
    mymap.add_place(eiffel_tower)
    mymap.add_place(louvre)
    mymap.add_place(cafe)
    mymap.add_place(park)
    
    # TODO 4: Show distances between places
    mymap.show_distances()
    
    # TODO 5: Save the map
    filename = mymap.save("my_favorite_places.html")
    
    # Open in browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)
    
    print("\n" + "=" * 50)
    print("✅ EXERCISE COMPLETE!")
    print("=" * 50)
    print("\nREFLECTION QUESTIONS:")
    print("1. How did Restaurant, Park, and Museum INHERIT from Place?")
    print("2. How is POLYMORPHISM shown when adding places to the map?")
    print("3. What data and methods are ENCAPSULATED in the Place class?")
    print("4. What complexity does the MyMap class ABSTRACT away?")
    print("\n🎯 BONUS: Try adding your own real favorite places!")


# ============================================================================
# BONUS: Challenge yourself!
# ============================================================================

"""
BONUS CHALLENGE 1: Add a new place type
Create a "Cafe" class that inherits from Restaurant
- Add a new attribute: has_wifi (True/False)
- Override get_popup_text() to include wifi info

BONUS CHALLENGE 2: Find the closest places
Write a function that finds the two closest places on your map

BONUS CHALLENGE 3: Add markers for YOUR city
Look up coordinates for your favorite places in YOUR city
Use Google Maps to find coordinates (right-click on a place)
"""

if __name__ == "__main__":
    main()