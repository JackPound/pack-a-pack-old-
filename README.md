# pack-a-pack
live link coming soon

Track your trips, backpacks, and the items packed in them! 

# Models
* Trip - Add a trip, with name, location, notes, and the backpacks you are taking with you.
* Backpack - Add your backpacks, with their size.
* Items - There is a database full of common backpacking items, that you can virtually pack into your backpacks. They have a size associated with them so you can plan what to take with you in your bag, or track your current pack contents while out on your trip!

# Current usability
* Users auth through Django, creating users with associated backpacks and trips. 
* Trips can be created, and your backpacks added to them.
* Backpacks can be created and packed with items from the item database. 
* Backpack tracks and displays how full it is based on items currently packed. 

# Planned features
* Users can add unique items visible and usable by only them. I.E. Their lucky can opener they bring on every trip.
* Items can be filtered and sorted while packing your bag. Currently displayed alphabetically, but would like to sort by size, category, quantity currently in bag, popular items/missing items. Recommendations (did you remember to pack a toothbrush?).
* Update trip notes, so you can leave notes like "Need to buy hiking boots" then once you buy them you can remove that from your trip notes. 
* Styling is minimal ATM, can always use better design. 
* Drag 'n' drop items to and from backpack for packing rather than simple + and x buttons.
* Functionality related to backpack space. A meter display for how packed it is, and explicit notifications when it is overpacked.
* Add 404 page.
* Add about or other refrences to my work.

# Tech Used
* Python
* Django
* PostgreSQL

