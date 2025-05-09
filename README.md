# Holiday Store  

# Overview  
**Holiday Store** is a themed shopping system that sells a variety of holiday-related products, including **toys, stuffed animals, and candy**. Each product is categorized by holiday, offering a unique shopping experience for different festive seasons.  

Abstract Factory Pattern in Holiday Store
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related objects without specifying their concrete classes. In our Holiday Store system, this pattern ensures that each holiday (Halloween, Christmas, Easter) can produce its own unique toys, stuffed animals, and candy, while maintaining a consistent structure for all products.

## Features  
- **Supports multiple holiday themes**: 🎃 Halloween, 🎄 Christmas, 🐰 Easter  
- **Product Categories**:  
  - **Toys**  
  - **Stuffed Animals**  
  - **Candy**  
- **Inventory Management**:  
  - Tracks stock levels  
  - Replenishes stock when running low  
  - Generates **Daily Transaction Reports (DTR)**  
- **Error Handling**:  
  - **InvalidDataError**: Ensures product attributes are valid  
  - **OrderError**: Handles cases where orders contain invalid data  

---

## 📂 Project Structure  
holiday_store/ │── assignmentFolder/ │ │── Items.py # Base class for all store items
│ │── Toy.py # Base class for toy items
│ │── StuffedAnimal.py # Base class for stuffed animals
│ │── Candy.py # Base class for candy items
│ │── ThemeFactory.py # Abstract factory for themed items
│── Store.py # Handles inventory & transactions
│── OrderProcessor.py # Processes orders from Excel files
│── InvalidDataError.py # Custom exception for invalid data
│── OrderError.py # Custom exception for order errors
│── products/ │ │── RCSpider.py # Halloween: Remote-controlled spider
│ │── Reindeer.py # Christmas: Stuffed reindeer
│ │── RobotBunny.py # Easter: Robotic bunny
│ │── SantasWorkshop.py # Christmas: Santa’s Workshop toy
│ │── PumpkinCaramel.py # Halloween: Pumpkin-flavored caramel
│ │── CandyCanes.py # Christmas: Traditional candy canes
│ │── CremeEgg.py # Easter: Chocolate creme-filled egg
│── README.md # Project documentation



---

# User Menu  
When the program runs, it provides a **terminal menu** that the store owner can use:  

1️⃣ **Process Web Orders**  
   - The store owner downloads an **Excel file** of all the online orders placed that day and processes them using the system.  

2️⃣ **Check Inventory**  
   - Displays all items in stock and their **status indicator**:  
     - **In Stock**: 10 or more items available  
     - **Low**: Less than 10 items  
     - **Very Low**: Less than 3 items  
     - **Out of Stock**: 0 items  

3️⃣ **Exit**  
   - Exits the program and generates a **Daily Transaction Report (DTR)**.  

---

# Product Details  

# 🎃 **Halloween**  
1. **RC Spider** *(Remote-Controlled Toy)*  
   - Battery Operated: **Yes**  
   - Speed: Customizable  
   - Jump Height: Adjustable  
   - Glow Feature: Optional  
   - Spider Type: **Tarantula** 🕷️ or **Wolf Spider** 🕸️  

2. **Pumpkin Caramel Toffee** *(Candy)*  
   - Lactose Free: **No**  
   - Contains Nuts: **May Contain Nuts**  
   - Variety: **Sea Salt or Regular**  

3. **Dancing Skeleton** *(Stuffed Animal)*  
   - Stuffing: **Polyester Fibrefill**  
   - Fabric: **Acrylic**  
   - Size: **S, M, L**  
   - Glow Feature: **Yes**  

---

# 🎄 **Christmas**  
1. **Santa’s Workshop** *(Toy Set)*  
   - Battery Operated: **No**  
   - Dimensions: Customizable  
   - Number of Rooms: Varies  

2. **Candy Canes** *(Candy)*  
   - Lactose Free: **Yes**  
   - Contains Nuts: **No**  
   - Stripes Color: **Red or Green**  

3. **Reindeer** *(Stuffed Animal)*  
   - Stuffing: **Wool**  
   - Fabric: **Cotton**  
   - Size: **S, M, L**  
   - Glow Feature: **Yes (Nose)**  

---

# 🐰 **Easter**  
1. **Robot Bunny** *(Interactive Toy)*  
   - Battery Operated: **Yes**  
   - Sound Effects: Multiple  
   - Color: **Orange, Blue, Pink**  

2. **Creme Eggs** *(Candy)*  
   - Lactose Free: **No**  
   - Contains Nuts: **May Contain Nuts**  
   - Pack Size: **Varies**  

3. **Easter Bunny** *(Stuffed Animal)*  
   - Stuffing: **Polyester Fibrefill**  
   - Fabric: **Linen**  
   - Size: **S, M, L**  
   - Color: **White, Grey, Pink, Blue**  

---

# 🔧 How It Works  

# 🏬 **Inventory Management**  
- **Adding Products**: When a product is first ordered, it is stocked with **100 units**.  
- **Replenishment**: If stock gets low, **an additional 100 units** are added automatically.  

# 🛒 **Order Processing**  
1. The store owner downloads an **Excel file** of online orders.  
2. The system reads the file using **pandas** and processes each order.  
3. If an item is **out of stock**, the system **orders more from the factory**.  
4. Orders are saved in the **Daily Transaction Report (DTR)**.  

# 📋 **Generating Reports**  
- The system automatically generates a daily transaction report summarizing all sales.  
  


