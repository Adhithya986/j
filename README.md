# Eclipse IDE Java Workspace (Stealth Lab & Exam Portal)

An ultra-realistic web portal modeled after the **Eclipse IDE for Java Developers**, containing all Java programs from:
1. **`java r 1.pdf`** - Vignana Bharathi Institute of Technology (VBIT) Java Lab Record (11 core experiments + 10 additional programs = 21 programs)
2. **`jajajajaj.pdf`** - Exam-Ready Java Programs & Concept Revision Guide (17 programs + 1 revision guide = 18 modules)
3. **`JDBC.pdf`** - Complete JDBC CRUD Operations Reference (5 programs)
**Total: 44 complete, compilable Java programs and modules.**

---

## 🚀 Quick Start

You can open and use the website immediately in several ways:

### Method 1: Instant Stealth Desktop App (Recommended)
Double-click **`run_eclipse.bat`** in this folder:
- Opens the portal in Google Chrome or Microsoft Edge **App Mode** (`--app`).
- **No address bar, no browser tabs, no bookmarks bar** — it launches as an authentic standalone Eclipse desktop window!
- Press **F11** or click the titlebar maximize button to go full screen for 100% stealth.

### Method 2: Double-Click File
Double-click **`index.html`** in File Explorer to open it in any browser (no server needed, works completely offline).

### Method 3: Local HTTP Server
Run the included python script:
```bash
python server.py
```
Then visit: `http://localhost:8080`

---

## 🕵️ Stealth Eclipse IDE Design Features

Designed so anyone glancing over your shoulder will see standard **Eclipse IDE**:
- **Authentic Eclipse Layout**:
  - Top title bar: `workspace - Java - Java_Lab_Record/src/lab/experiments/ForDemo.java - Eclipse IDE`
  - Window controls (Minimize, Maximize, Close)
  - Full Menu Bar: `File`, `Edit`, `Source`, `Refactor`, `Navigate`, `Search`, `Project`, `Run`, `Window`, `Help` with working dropdowns
  - Toolbar with authentic Eclipse icons: Save, Save All, Run (green play), Debug (green bug), Search (flashlight), Perspectives (`Java`, `Debug`)
- **Package Explorer Tree (Left Panel)**:
  - Exact Eclipse tree hierarchy: Projects (`📁`), Source folders (`src`), Packages (`📦`), Classes (`Ⓒ`), Interfaces (`Ⓘ`), JRE Libraries (`☕`), and JARs (`📦`).
  - Live filter input (`type filter text`).
- **Multi-Tab Java Editor (Center Panel)**:
  - Tabs with file icons, close `×` button, active tab indicator.
  - Breadcrumbs path bar (`Project > src > package > Class > method`).
  - Line numbers gutter with **clickable red breakpoint dots**.
  - Java syntax highlighting with authentic Eclipse typography (Consolas font).
- **Console & Problems View (Bottom Panel)**:
  - `<terminated> ClassName [Java Application] C:\Program Files\Java\jdk-17\bin\javaw.exe` header.
  - Exact simulated program outputs matching the lab manual and exam PDFs.
  - "Problems" view showing `0 errors, 0 warnings`.
  - "Javadoc / Info" view showing problem statement, concepts, and algorithm notes.
  - Embedded "Terminal" view.
- **Theme Switcher**:
  - Toggle between **Eclipse Dark Theme** (default) and **Eclipse Light Classic Theme** via toolbar button or `Window > Toggle Theme`.
- **Full-Screen Stealth (F11)**:
  - Hides browser chrome so the entire monitor appears to be Eclipse IDE.

---

## 📋 One-Click Copy Features

- **Large "Copy Code" Button**: Located right on the editor action bar. One click copies the clean, complete Java source code to your clipboard.
- **Toolbar Quick Copy**: Prominent "Copy Code" button in the top toolbar.
- **Keyboard Shortcut**: Press **`Alt+C`** to copy the current code instantly.
- **Package Explorer Right-Click**: Right-click on any file in the tree to copy its code immediately.
- **Copy Console Output**: Dedicated button in the Console panel to copy execution results.
- **Save .java**: Dedicated button to download the pure `.java` file with proper filename.

---

## 🔍 Fast Search Capabilities

1. **Quick Access Search (`Ctrl+3`)**:
   - Located in the top-right toolbar.
   - Start typing to search across class names, experiment numbers, keywords, and topics with instant autocomplete dropdown.
2. **Package Explorer Live Filter**:
   - Located at the top of the tree view.
   - Filters projects, packages, and files in real-time as you type.
3. **Open Resource / Search Modal (`Ctrl+Shift+R` or `Ctrl+H`)**:
   - Classic Eclipse dialog modal.
   - Full keyboard navigation (type to filter, up/down arrows, Enter to open).

---

## 📚 Complete Program Catalog (44 Programs)

### 1. Java Lab Record (`java r 1.pdf`)
| File Name | Experiment / Topic | Description |
|-----------|--------------------|-------------|
| `ForDemo.java` | Experiment 1 | Armstrong number check using `for` loop and `if-else` |
| `StringBufferDemo.java` | Experiment 2 | Palindrome string check using `StringBuffer.reverse()` |
| `MethodOverloadingDemo.java` | Experiment 3 | Method Overloading with `Person` class `setInput()` |
| `ConstructorOverloadingDemo.java` | Experiment 4 | Constructor Overloading with `Person` class |
| `Polymorphism1.java` | Experiment 5 | Method Overriding (Runtime Polymorphism) |
| `Inheritance3.java` | Experiment 6 | `this` and `super` keyword constructor chaining |
| `UsingPackages.java` | Experiment 7a | User-defined package `pack` (`Additionpack`, `Substractionpack`) |
| `MultipleInterface.java` | Experiment 7b | Multiple Inheritance using Interfaces |
| `AbstractClasses.java` | Experiment 8 | Abstract class `MyClass` (Square, Square Root, Cube) |
| `RandomTest.java` | Experiment 9 | 3 Threads application (Random generator, Square, Cube) |
| `DoublyLinkedListDeletion.java` | Experiment 10 | Doubly Linked List creation, insert, delete, and display |
| `DisplayFiles.java` | Additional 1 | Recursive directory file and subdirectory listing |
| `DisplayTableAWT.java` | Additional 2 | Display comma-separated table data using AWT Frame |
| `DisplayTableFromFile.java` | Additional 3 | Display table from file using Swing `JFrame` and `JScrollPane` |
| `IntegerDivision.java` | Additional 4 | Integer division GUI with `NumberFormatException` & `ArithmeticException` |
| `MouseListenerDemo.java` | Additional 5 | AWT Frame implementing `MouseListener` (5 mouse events) |
| `MyApplet.java` | Additional 6 | Applet greeting demo using `paint()` |
| `PhoneDirectory.java` | Additional 7 | Two-way phone directory search using `Hashtable` |
| `SimpleCalculator.java` | Additional 8 | Swing GUI Calculator with 4x4 GridLayout keypad |
| `TestApplet.java` | Additional 9 | Applet lifecycle methods: `init()`, `start()`, `paint()` |
| `TrafficLightSimulator.java` | Additional 10 | Swing Traffic Light simulator with `JRadioButton` Red, Yellow, Green |

### 2. Exam-Ready Programs (`jajajajaj.pdf`)
| File Name | Question / Topic | Description |
|-----------|------------------|-------------|
| `ShapeDemo.java` | Question 1 | Abstract class `Shape` with `Rectangle`, `Triangle`, `Circle` |
| `MultilevelDemo.java` | Question 2 | Multilevel inheritance: `GrandFather` → `Father` → `Son` |
| `FinalDemo.java` | Question 3 | `final` variable and `final` method demonstration |
| `Palindrome.java` | Question 4 | `StringBuffer` mutability to check Palindrome |
| `AbstractDemo.java` | Question 5 | Abstract class `Animal` with abstract `sound()` and concrete `eat()` |
| `SuperDemo.java` | Question 6 | `super` keyword to access parent variable & parent method |
| `PackageDemo.java` | Question 7 | User-defined package `sample` with `Test` class |
| `InterfaceDemo.java` | Question 8 | `interface Animal` implemented by class `Dog` |
| `UserExceptionDemo.java` | Question 9 | Custom `AgeException` using `throw` keyword |
| `MultipleInheritanceDemo.java` | Question 10 | Multiple inheritance via interfaces `Father` & `Mother` |
| `HierarchicalDemo.java` | Question 11 | Hierarchical inheritance: `Animal` → `Dog`, `Cat` |
| `ThrowsDemo.java` | Question 12 | Exception handling using `throws` declaration |
| `SingleInheritanceDemo.java` | Question 13 | Single inheritance: `Animal` → `Dog` |
| `MultipleCatchDemo.java` | Question 14 | Multiple catch blocks (`ArrayIndexOutOfBoundsException`, etc.) |
| `Armstrong.java` | Question 15 | Armstrong number check using `if-else` and `for` loop |
| `VehicleDemo.java` | Question 16 | `interface Vehicle` implemented by `Car` and `Bike` |
| `FinallyDemo.java` | Question 17 | Exception handling with `try`, `catch`, and `finally` block |
| `QuickExamRevision.java` | Revision Guide | Comprehensive 14-topic Java OOP & keyword concept matrix |

### 3. JDBC Database Operations (`JDBC.pdf`)
| File Name | CRUD Operation | Description |
|-----------|----------------|-------------|
| `CreateTable.java` | CREATE | `CREATE TABLE student (id INT, name VARCHAR(30))` |
| `InsertData.java` | INSERT | `INSERT INTO student VALUES (1, 'Ravi')` |
| `SelectData.java` | SELECT | `SELECT * FROM student` with `ResultSet` iteration |
| `UpdateData.java` | UPDATE | `UPDATE student SET name = 'Surya' WHERE id = 1` |
| `DeleteData.java` | DELETE | Parameterized `DELETE` using `PreparedStatement` & `Scanner` |

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **`Alt+C`** | **Copy Current Java Code to Clipboard** |
| **`Ctrl+3`** | **Focus Quick Access Search Bar** |
| **`Ctrl+Shift+R`** / **`Ctrl+H`** | **Open Resource / Search Modal** |
| **`Ctrl+F11`** | **Run Current Program (Console Simulation)** |
| **`F11`** | **Toggle Fullscreen Stealth Mode** |
| **`Ctrl+W`** | **Close Active Editor Tab** |
| **`Ctrl+S`** | **Save Workspace** |

