# 🎨 Color Palette Database  
*A SQL-based web app for organizing, exploring, and visualizing color palettes.*
Created for my personalized final project for the BYU CS452 Database Modeling Concepts class

---

## 📘 Overview
The **Color Palette Database** is a creative data management project that allows users to create, store, and browse custom color palettes.  
Each palette can include multiple colors, tags, and descriptions, enabling artists, designers, and crafters to organize their inspiration in one searchable place.

This project demonstrates **relational database modeling, SQL queries, and CRUD operations** using PostgreSQL and Flask.  
It was developed as a final project for a **Database Modeling Concepts** course.

---

## 💡 Features
- Create, view, edit, and delete color palettes  
- Store individual colors with HEX, RGB, and hue data  
- Tag palettes by theme, mood, or use case (e.g., *"vintage"*, *"modern"*)  
- Search palettes by color or tag  
- Visual display of palettes using CSS color blocks  
- (Optional) Filter or sort palettes by hue, brightness, or saturation  

---

## 🧩 Database Schema

**Core Tables**
- `palettes` — stores palette information  
- `colors` — stores color properties (hex, rgb, hue, etc.)  
- `palette_colors` — many-to-many relationship between palettes and colors  
- `tags` — stores tags or categories  
- `palette_tags` — many-to-many relationship between palettes and tags  

**Relationships**
- Each palette can include many colors and many tags  
- Each color can appear in multiple palettes  
- Each tag can apply to multiple palettes  

![ER Diagram Placeholder](docs/er-diagram.png)
> (Include your ER diagram image or link here once created)

---

## 🧰 Technologies Used
| Layer | Technology | Purpose |
|--------|-------------|----------|
| Database | **PostgreSQL** (or SQLite) | Main SQL database |
| Backend | **Python (Flask)** | API + database connection |
| Frontend | **HTML, CSS, JavaScript** | Display palettes and forms |
| Version Control | **Git + GitHub** | Version tracking and public repo |
| Optional | **Chart.js / Tailwind CSS** | Data visualization or styling |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/color-palette-database.git
cd color-palette-database

