# 🎨 Final Report — Color Palette Database

## 📝 Project Summary
The **Color Palette Database** is a SQL-powered web application that allows users to create, browse, edit, and delete custom color palettes. It demonstrates relational database design, CRUD operations, backend–frontend integration using Flask, and UI/UX considerations for visual color data. Users can log in, manage palettes, and view color blocks in a clean, responsive interface.

---

## 📊 Designs & Visuals

### **System Diagram**
![ER Diagram](color-palette-db-schema.png)


### 🧰 System Design - Technologies Used
| Layer | Technology | Purpose |
|--------|-------------|----------|
| Database | **MySql** (or SQLite) | Main SQL database |
| Backend | **Python (Flask)** | API + database connection |
| Frontend | **HTML, CSS, JavaScript** | Display palettes and forms |
| Version Control | **Git + GitHub** | Version tracking and public repo |
| Optional WebHosting Platform | **Render** or **PythonAnywhere** | Hosting the webpage and Database |

<img width="391" height="311" alt="palette_system_design drawio" src="https://github.com/user-attachments/assets/66be9b43-9725-4417-8020-d690e681d5e4" />



### **UI Sketches**
  <img width="961" height="491" alt="palette_login drawio" src="https://github.com/user-attachments/assets/2d4db96f-01aa-4504-b448-b04f210fff7a" />

  <img width="961" height="492" alt="palette_selector drawio" src="https://github.com/user-attachments/assets/93ac6fc0-2459-4e23-a9aa-05298d66bfab" />

  <img width="961" height="492" alt="palette_edit_delete drawio" src="https://github.com/user-attachments/assets/419a78db-160d-430c-a0cc-6e7c066ad05c" />

  <img width="961" height="492" alt="palette_editpalette drawio" src="https://github.com/user-attachments/assets/86f8b765-26b4-4e6e-adab-627a2326a692" />
  
---

## ▶️ Demo
![Demo Video](https://youtu.be/nFpsq9jgTgw)
![DatabseQueryVideo](https://youtu.be/jhzR49yzK78)

---

## 📘 What I Learned

Throughout this project, I learned how to design and implement a real relational database and connect it to a functioning web application. Some core learnings include:

### **1. Database Modeling & Constraints**
- Creating an ERD and translating it into SQL tables.
- Applying foreign keys, many-to-many relationships, and cascading behaviors.
- Understanding how design choices affect query efficiency and UX.

### **2. Full CRUD With Flask**
- Handling form submissions and writing secure SQL queries.
- Sending data between templates and backend routes.
- Debugging issues related to routing, POST/GET handling, and template rendering.

### **3. Frontend Interaction & UI Design**
- Displaying palettes visually using CSS-generated color blocks.
- Creating dynamic elements (e.g., side panels, tooltips).
- Using JavaScript to enhance interactivity and improve workflow.

---

## 🤖 AI Integration

### **Does this project integrate AI directly?**
No — the application itself does not use AI tools in production.

### **How AI assisted in building the project**
AI was used as a **development partner**, helping with:
- Debugging Flask routing issues.
- Suggesting improved UI/UX approaches.
- Refining CSS for layout consistency.
- Creating schema diagrams and explaining relational modeling.
- Providing example SQL queries and validation logic.
- Brainstorming UX ideas (icons, buttons, layout patterns).
- Generating documentation drafts

AI support made iteration faster, especially for debugging and redesigning UI components.

---

## ⭐ Why This Project Was Interesting to Me

I love design, color theory, and organization tools, so building a project centered around **colors and palettes** was naturally enjoyable. It let me combine creativity with technical skills—databases, backend logic, and UI styling. The project also let me make something *personally useful*, since color picking and palette organization are helpful for art, design projects, crafting, and coding themes.

---

## 🧩 Key Learnings

1. **Database constraints are essential**  
   Unique palette names, required fields, and foreign keys are crucial to preventing bad data.

2. **Frontend and backend consistency matters**  
   Even small UI changes (like how a panel expands or where a button sits) can reveal deeper logic issues.

3. **Iterating is part of the process**  
   Layouts, SQL joins, and CSS positioning broke multiple times—and fixing them helped me understand the system fully.

4. **Understanding routing and state**  
   Managing logged-in users, preserving session context, and navigating between pages was a big part of the project.

5. **Real full-stack development involves constant debugging**  
   I learned how databases, Flask, and client-side scripts interact (or fail to), giving me a clearer view of the full app stack.

---

## ⚙️ Extra Notes on Performance / Architecture

Even though this is a small project, the design prepares for scalability (though this is still in progress):

- **Normalized schema** prevents duplicate color data (this still needs to be adjusted).
- **Many-to-many pivot tables** allow efficient palette/tag/color relationships.
- **Prepared statements & parameterized queries** (via Flask) protect against SQL injection.
- **Modular route structure** improves readability and debugging.
- **Potential scalability**:
  - Indexes can be added to palette-color tables for faster lookups.
  - Hosting on Render/PythonAnywhere would support larger datasets.
  - Concurrency for multiple users is handled through Flask’s request isolation.

Authentication uses simple username-based login for now, but could be extended to:
- hashed passwords,
- session tokens,
- and role-based permissions.

---


## Future Work:

### Near Future:
I hope to work on the following:
- Fixing the database so that palette names (at least palette_name and username) and color names are unique
- Added a user_color table to the database so the user can see their own colors
- Allowing the user to create, update, delete their own colors (but not other's colors)
- Add functionality so the user can create tags and add them to palettes (and be able to query palettes by tags)

### Items To Complete Afterwards
- Update authentication to hash the passwords
- Create a register screen instead of just login
- Search palettes by color or tag
- Generate palette from imported picture
- Download palette (with hex values) for printing
- (Stretch goal) find colors that are similar or colors that have been with a certain color on a palette
- Implement this as a public web application using Render or PythonAnywhere

