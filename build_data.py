# -*- coding: utf-8 -*-
"""
Script to compile all 43 Java programs from the 3 PDFs:
1. jajajajaj.pdf (17 exam programs + Quick Revision)
2. java r 1.pdf (21 lab record programs)
3. JDBC.pdf (5 CRUD operations)
"""

import json

programs = [
    # =========================================================================
    # GROUP 1: Vignana Bharathi Institute of Technology - Lab Record (java r 1.pdf)
    # =========================================================================
    {
        "id": "lab_exp_01",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "ForDemo.java",
        "className": "ForDemo",
        "title": "Experiment 1: Armstrong Number (For Loop & If-Else)",
        "experimentNo": "Experiment 1",
        "sourcePdf": "java r 1.pdf",
        "description": "Acquaint with Eclipse platform, debugging step by step with small program containing at least one if-else condition and for loop to check if a number is an Armstrong number.",
        "tags": ["for loop", "if else", "armstrong", "scanner", "basics", "math"],
        "code": """import java.util.Scanner;

public class ForDemo {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        int n = sc.nextInt();
        int t = n;
        int sum = 0;
        for (int temp = n; temp != 0; temp = temp / 10) {
            int r = temp % 10;
            sum = sum + r * r * r;
        }
        if (sum == t) {
            System.out.println("Armstrong");
        } else {
            System.out.println("Not a Armstrong");
        }
        sc.close();
    }
}""",
        "output": """Enter the number:
153
Armstrong"""
    },
    {
        "id": "lab_exp_02",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "logicBuilding",
        "fileName": "StringBufferDemo.java",
        "className": "StringBufferDemo",
        "title": "Experiment 2: StringBuffer Mutability (Palindrome)",
        "experimentNo": "Experiment 2",
        "sourcePdf": "java r 1.pdf",
        "description": "Demonstrate mutability of StringBuffer class to find out whether a given string is palindrome or not.",
        "tags": ["stringbuffer", "palindrome", "mutability", "reverse", "io", "string"],
        "code": """package logicBuilding;

import java.io.*;

public class StringBufferDemo {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the String:");
        String str1 = br.readLine();
        StringBuffer sb = new StringBuffer(str1);
        sb.reverse();
        String str2 = String.valueOf(sb);
        System.out.println(str2);
        if (str1.equals(str2))
            System.out.println("Palindrome");
        else
            System.out.println("Not a Palindrome");
    }
}""",
        "output": """Enter the String:
272
272
Palindrome"""
    },
    {
        "id": "lab_exp_03",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "MethodOverloadingDemo.java",
        "className": "MethodOverloadingDemo",
        "title": "Experiment 3: Method Overloading",
        "experimentNo": "Experiment 3",
        "sourcePdf": "java r 1.pdf",
        "description": "Write a java program to demonstrate Method Overloading using Person class with different setInput parameters.",
        "tags": ["method overloading", "polymorphism", "compile time polymorphism", "oops", "methods"],
        "code": """class Person {
    private String name;
    private int age;

    void setInput() {
        name = "Arjun";
        age = 20;
    }

    void setInput(String nam) {
        name = nam;
        age = 25;
    }

    void setInput(String nam, int ag) {
        name = nam;
        age = ag;
    }

    public void talk() {
        System.out.println("Name=" + name);
        System.out.println("age=" + age);
    }
}

public class MethodOverloadingDemo {
    public static void main(String args[]) {
        System.out.println("Welcome to Java");
        Person p1 = new Person();
        p1.setInput();
        p1.talk();
        Person p2 = new Person();
        p2.setInput("Raju");
        p2.talk();
        Person p3 = new Person();
        p3.setInput("Rani", 22);
        p3.talk();
    }
}""",
        "output": """Welcome to Java
Name=Arjun
age=20
Name=Raju
age=25
Name=Rani
age=22"""
    },
    {
        "id": "lab_exp_04",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "ConstructorOverloadingDemo.java",
        "className": "ConstructorOverloadingDemo",
        "title": "Experiment 4: Constructor Overloading",
        "experimentNo": "Experiment 4",
        "sourcePdf": "java r 1.pdf",
        "description": "Write a java program to demonstrate Constructor Overloading using Person class.",
        "tags": ["constructor overloading", "constructors", "oops", "overloading"],
        "code": """class Person {
    private String name;
    private int age;

    Person() {
        name = "Surya";
        age = 18;
    }

    Person(String nam) {
        name = nam;
        age = 25;
    }

    Person(String nam, int ag) {
        name = nam;
        age = ag;
    }

    public void talk() {
        System.out.println("Name=" + name);
        System.out.println("Age=" + age);
    }
}

public class ConstructorOverloadingDemo {
    public static void main(String args[]) {
        System.out.println("Welcome to Java");
        Person p1 = new Person();
        p1.talk();
        Person p2 = new Person("Raju");
        p2.talk();
        Person p3 = new Person("Rani", 22);
        p3.talk();
    }
}""",
        "output": """Welcome to Java
Name=Surya
Age=18
Name=Raju
Age=25
Name=Rani
Age=22"""
    },
    {
        "id": "lab_exp_05",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Inherit",
        "fileName": "Polymorphism1.java",
        "className": "Polymorphism1",
        "title": "Experiment 5: Method Overriding (Runtime Polymorphism)",
        "experimentNo": "Experiment 5",
        "sourcePdf": "java r 1.pdf",
        "description": "Write a java program to demonstrate Method Overriding (Dynamic Polymorphism) with Parent10 and Child10 classes.",
        "tags": ["method overriding", "polymorphism", "runtime polymorphism", "inheritance", "oops"],
        "code": """package Inherit;

class Parent10 {
    void marry() {
        System.out.println("Black");
    }
}

class Child10 extends Parent10 {
    @Override
    void marry() {
        System.out.println("Red");
    }
}

public class Polymorphism1 {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Child10 c = new Child10();
        c.marry();
    }
}""",
        "output": """Hello World!
Red"""
    },
    {
        "id": "lab_exp_06",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "Inheritance3.java",
        "className": "Inheritance3",
        "title": "Experiment 6: 'this' and 'super' Keywords",
        "experimentNo": "Experiment 6",
        "sourcePdf": "java r 1.pdf",
        "description": "Write a java program using 'this' and 'super' keywords for constructor chaining and inheritance invocation.",
        "tags": ["this", "super", "constructor chaining", "inheritance", "keywords"],
        "code": """class Parent11 {
    Parent11() {
        System.out.println("Parent class Zero Argument Constructor");
    }
}

class Child11 extends Parent11 {
    Child11() {
        this(10);
        System.out.println("Child class Zero Argument Constructor");
    }

    Child11(int a) {
        super();
        System.out.println("Child class One Argument Constructor");
    }
}

public class Inheritance3 {
    public static void main(String[] args) {
        System.out.println("Hello world!!");
        new Child11();
    }
}""",
        "output": """Hello world!!
Parent class Zero Argument Constructor
Child class One Argument Constructor
Child class Zero Argument Constructor"""
    },
    {
        "id": "lab_exp_07a",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Temp",
        "fileName": "UsingPackages.java",
        "className": "UsingPackages",
        "title": "Experiment 7a: User Defined Packages (pack)",
        "experimentNo": "Experiment 7a",
        "sourcePdf": "java r 1.pdf",
        "description": "Create a user defined package named 'pack' and demonstrate importing this package into another program.",
        "tags": ["package", "import", "user defined package", "modular", "pack"],
        "code": """package Temp;

// In package 'pack':
// public class Additionpack {
//     int a, b;
//     public Additionpack(int x, int y) { a = x; b = y; }
//     public void sum() { System.out.println("sum=" + (a + b)); }
// }
// public class Substractionpack {
//     private double d1, d2;
//     public Substractionpack(double d, double e) { d1 = d; d2 = e; }
//     public void sub() { System.out.println("Sub=" + (d1 - d2)); }
// }

class Additionpack {
    int a, b;

    public Additionpack(int x, int y) {
        a = x;
        b = y;
    }

    public void sum() {
        System.out.println("sum=" + (a + b));
    }
}

class Substractionpack {
    private double d1, d2;

    public Substractionpack(double d, double e) {
        d1 = d;
        d2 = e;
    }

    public void sub() {
        System.out.println("Sub=" + (d1 - d2));
    }
}

public class UsingPackages {
    public static void main(String args[]) {
        Additionpack obj1 = new Additionpack(50, 50);
        obj1.sum();
        Substractionpack obj2 = new Substractionpack(10.5, 45.5);
        obj2.sub();
    }
}""",
        "output": """sum=100
Sub=-35.0"""
    },
    {
        "id": "lab_exp_07b",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "MultipleInterface.java",
        "className": "MultipleInterface",
        "title": "Experiment 7b: Multiple Inheritance Using Interface",
        "experimentNo": "Experiment 7b",
        "sourcePdf": "java r 1.pdf",
        "description": "Demonstrate multiple inheritance in Java using interfaces (MyInterface3, MyInterface4).",
        "tags": ["interface", "multiple inheritance", "implements", "oops"],
        "code": """interface MyInterface3 {
    void greetings();
}

interface MyInterface4 {
    void greetings();
}

class MyClass4 implements MyInterface3, MyInterface4 {
    public void greetings() {
        System.out.println("Multiple inheritance using Interface");
    }
}

public class MultipleInterface {
    public static void main(String[] args) {
        MyClass4 obj1 = new MyClass4();
        obj1.greetings();
    }
}""",
        "output": """Multiple inheritance using Interface"""
    },
    {
        "id": "lab_exp_08",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "ABSTRACT",
        "fileName": "AbstractClasses.java",
        "className": "AbstractClasses",
        "title": "Experiment 8: Abstract Class & Derived Classes",
        "experimentNo": "Experiment 8",
        "sourcePdf": "java r 1.pdf",
        "description": "Demonstrate Abstract Class with MyClass and subclasses Sub1 (square), Sub2 (square root), Sub3 (cube).",
        "tags": ["abstract class", "abstract methods", "subclasses", "math", "oops"],
        "code": """package ABSTRACT;

abstract class MyClass {
    abstract void calculate(double x);
}

class Sub1 extends MyClass {
    void calculate(double x) {
        System.out.println("Square=" + (x * x));
    }
}

class Sub2 extends MyClass {
    void calculate(double x) {
        System.out.println("Square root=" + Math.sqrt(x));
    }
}

class Sub3 extends MyClass {
    void calculate(double x) {
        System.out.println("Cube=" + Math.pow(x, 3));
    }
}

public class AbstractClasses {
    public static void main(String args[]) {
        Sub1 obj1 = new Sub1();
        Sub2 obj2 = new Sub2();
        Sub3 obj3 = new Sub3();
        obj1.calculate(3);
        obj2.calculate(4);
        obj3.calculate(5);
    }
}""",
        "output": """Square=9.0
Square root=2.0
Cube=125.0"""
    },
    {
        "id": "lab_exp_09",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "RandomTest.java",
        "className": "RandomTest",
        "title": "Experiment 9: Multi-threaded Application (3 Threads)",
        "experimentNo": "Experiment 9",
        "sourcePdf": "java r 1.pdf",
        "description": "Multi-threaded application: 1st thread generates random integer every second; 2nd thread squares if even; 3rd thread cubes if odd.",
        "tags": ["multithreading", "thread", "runnable", "random", "synchronization", "sleep"],
        "code": """import java.util.Random;

class Sqthread extends Thread {
    int n;

    Sqthread(int num) {
        n = num;
    }

    public void run() {
        System.out.println("Square = " + (n * n));
    }
}

class cbthread extends Thread {
    int n;

    cbthread(int num) {
        n = num;
    }

    public void run() {
        System.out.println("Cube = " + (n * n * n));
    }
}

class Rthread extends Thread {
    public void run() {
        Random r = new Random();
        for (int i = 0; i < 5; i++) {
            int k = r.nextInt(20);
            System.out.println("Generated: " + k);
            if (k % 2 == 0) {
                Sqthread s = new Sqthread(k);
                s.start();
            } else {
                cbthread c = new cbthread(k);
                c.start();
            }
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}

public class RandomTest {
    public static void main(String args[]) {
        Rthread rt = new Rthread();
        rt.start();
    }
}""",
        "output": """Generated: 9
Cube = 729
Generated: 4
Square = 16
Generated: 5
Cube = 125
Generated: 3
Cube = 27
Generated: 10
Square = 100"""
    },
    {
        "id": "lab_exp_10",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "lab.experiments",
        "fileName": "DoublyLinkedListDeletion.java",
        "className": "DoublyLinkedListDeletion",
        "title": "Experiment 10: Doubly Linked List Deletion",
        "experimentNo": "Experiment 10",
        "sourcePdf": "java r 1.pdf",
        "description": "Create a doubly linked list of elements, delete a given element, and display contents after deletion.",
        "tags": ["data structures", "linked list", "doubly linked list", "pointers", "node", "deletion"],
        "code": """class DoublyLinkedList {
    class Node {
        int data;
        Node prev, next;

        Node(int data) {
            this.data = data;
            this.prev = null;
            this.next = null;
        }
    }

    private Node head;

    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
        newNode.prev = temp;
    }

    public void delete(int key) {
        Node temp = head;
        while (temp != null && temp.data != key) {
            temp = temp.next;
        }
        if (temp == null) {
            System.out.println("Element " + key + " not found.");
            return;
        }
        if (temp == head) {
            head = temp.next;
            if (head != null) head.prev = null;
        } else {
            if (temp.prev != null) temp.prev.next = temp.next;
            if (temp.next != null) temp.next.prev = temp.prev;
        }
        System.out.println("Element " + key + " deleted successfully");
    }

    public void display() {
        Node temp = head;
        if (temp == null) {
            System.out.println("List is empty");
            return;
        }
        System.out.println("Doubly Linked list:");
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }
}

public class DoublyLinkedListDeletion {
    public static void main(String args[]) {
        DoublyLinkedList list = new DoublyLinkedList();
        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insert(40);
        list.insert(50);
        System.out.println("Before Deleting");
        list.display();
        list.delete(30);
        System.out.println("After Deleting");
        list.display();
    }
}""",
        "output": """Before Deleting
Doubly Linked list:
10
20
30
40
50
Element 30 deleted successfully
After Deleting
Doubly Linked list:
10
20
40
50"""
    },
    {
        "id": "lab_add_01",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "DisplayFiles.java",
        "className": "DisplayFiles",
        "title": "Additional 1: Recursive Directory & File Display",
        "experimentNo": "Additional Program 1",
        "sourcePdf": "java r 1.pdf",
        "description": "Recursively prints all files and subdirectories from a given directory with tree indentation.",
        "tags": ["file io", "recursion", "file handling", "directory", "tree"],
        "code": """package Java_Lab;

import java.io.File;

public class DisplayFiles {
    public void printFiles(File[] a, int i, int lvl) {
        // base case of the recursion
        if (i == a.length) {
            return;
        }
        // tabs for indentation
        for (int j = 0; j < lvl; j++) {
            System.out.print("\\t");
        }
        // checking if file or directory
        if (a[i].isFile()) {
            System.out.println(a[i].getName());
        } else if (a[i].isDirectory()) {
            System.out.println("[" + a[i].getName() + "]");
            File[] sub = a[i].listFiles();
            if (sub != null) {
                printFiles(sub, 0, lvl + 1);
            }
        }
        printFiles(a, i + 1, lvl);
    }

    public static void main(String[] argvs) {
        String path = "D:\\\\Java Programs";
        File f = new File(path);
        DisplayFiles obj = new DisplayFiles();
        if (f.exists() && f.isDirectory()) {
            File[] arr = f.listFiles();
            System.out.println("Files from directory: " + f);
            if (arr != null) obj.printFiles(arr, 0, 0);
        } else {
            System.out.println("Directory does not exist.");
        }
    }
}""",
        "output": """Files from directory: D:\\Java Programs
[Core_Java]
\tsrc
\t\tForDemo.java
\t\tPhone.txt
DisplayFiles.java"""
    },
    {
        "id": "lab_add_02",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "DisplayTableAWT.java",
        "className": "DisplayTableAWT",
        "title": "Additional 2: Table Display using AWT",
        "experimentNo": "Additional Program 2",
        "sourcePdf": "java r 1.pdf",
        "description": "Reads comma-separated values from a text file and renders them in an AWT Frame with GridLayout.",
        "tags": ["awt", "gui", "gridlayout", "file reading", "scanner"],
        "code": """package Java_Lab;

import java.awt.*;
import java.io.File;
import java.util.Scanner;

public class DisplayTableAWT extends Frame {
    public DisplayTableAWT() {
        setTitle("Table Display using AWT");
        setSize(600, 400);
        setLayout(new GridLayout(4, 4, 10, 10));
        try {
            File file = new File("D:\\\\Table.txt");
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] items = line.split(",");
                for (String data : items) {
                    Label lbl = new Label(data.trim());
                    lbl.setBackground(Color.LIGHT_GRAY);
                    add(lbl);
                }
            }
            sc.close();
        } catch (Exception e) {
            add(new Label("Error: " + e.getMessage()));
        }
        setVisible(true);
    }

    public static void main(String[] args) {
        new DisplayTableAWT();
    }
}""",
        "output": """[AWT Frame window opened: Table Display using AWT (600x400)]"""
    },
    {
        "id": "lab_add_03",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "DisplayTableFromFile.java",
        "className": "DisplayTableFromFile",
        "title": "Additional 3: Table Display from File (Swing)",
        "experimentNo": "Additional Program 3",
        "sourcePdf": "java r 1.pdf",
        "description": "Reads data from a CSV/text file into a dynamic Swing grid layout with styled header and cells.",
        "tags": ["swing", "jframe", "jscrollpane", "csv", "table", "gui"],
        "code": """package Java_Lab;

import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.util.*;

public class DisplayTableFromFile extends JFrame {
    public DisplayTableFromFile() {
        setTitle("Table Display from File");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 400);
        setLayout(new BorderLayout());

        JPanel panel = new JPanel();
        JScrollPane scrollPane = new JScrollPane(panel);

        try {
            File file = new File("Table.txt");
            Scanner sc = new Scanner(file);
            java.util.List<String[]> rows = new ArrayList<>();
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] columns = line.split(",");
                rows.add(columns);
            }
            sc.close();

            if (rows.isEmpty()) {
                JOptionPane.showMessageDialog(this, "The file is empty!", "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            int cols = rows.get(0).length;
            panel.setLayout(new GridLayout(rows.size(), cols, 5, 5));

            for (int i = 0; i < rows.size(); i++) {
                for (int j = 0; j < cols; j++) {
                    JLabel label = new JLabel(rows.get(i)[j].trim(), SwingConstants.CENTER);
                    label.setOpaque(true);
                    if (i == 0) {
                        label.setBackground(Color.LIGHT_GRAY);
                        label.setFont(new Font("Arial", Font.BOLD, 14));
                    } else {
                        label.setBackground(Color.WHITE);
                        label.setFont(new Font("Arial", Font.PLAIN, 13));
                    }
                    label.setBorder(BorderFactory.createLineBorder(Color.GRAY));
                    panel.add(label);
                }
            }
        } catch (FileNotFoundException e) {
            JOptionPane.showMessageDialog(this, "File not found!", "Error", JOptionPane.ERROR_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Error reading file: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }

        add(scrollPane, BorderLayout.CENTER);
        setVisible(true);
    }

    public static void main(String[] args) {
        new DisplayTableFromFile();
    }
}""",
        "output": """[Swing Frame window launched: Table Display from File with JScrollPane grid]"""
    },
    {
        "id": "lab_add_04",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "IntegerDivision.java",
        "className": "IntegerDivision",
        "title": "Additional 4: Integer Division GUI with Exception Dialogs",
        "experimentNo": "Additional Program 4",
        "sourcePdf": "java r 1.pdf",
        "description": "Swing GUI calculator for integer division with NumberFormatException and ArithmeticException JOptionPane dialogs.",
        "tags": ["swing", "exception handling", "arithmeticexception", "numberformatexception", "gui", "joptionpane"],
        "code": """package Java_Lab;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class IntegerDivision extends JFrame implements ActionListener {
    JTextField num1Field, num2Field, resultField;
    JButton divideButton;
    JLabel num1Label, num2Label, resultLabel;

    public IntegerDivision() {
        setTitle("Integer Division");
        setLayout(new GridLayout(4, 2, 10, 10));

        num1Label = new JLabel("Num1:");
        num2Label = new JLabel("Num2:");
        resultLabel = new JLabel("Result:");

        num1Field = new JTextField();
        num2Field = new JTextField();
        resultField = new JTextField();
        resultField.setEditable(false);

        divideButton = new JButton("Divide");
        divideButton.addActionListener(this);

        add(num1Label);
        add(num1Field);
        add(num2Label);
        add(num2Field);
        add(resultLabel);
        add(resultField);
        add(new JLabel(""));
        add(divideButton);

        setSize(350, 200);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            int num1 = Integer.parseInt(num1Field.getText());
            int num2 = Integer.parseInt(num2Field.getText());
            int result = num1 / num2;
            resultField.setText(String.valueOf(result));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this,
                    "Please enter valid integers!",
                    "Number Format Error",
                    JOptionPane.ERROR_MESSAGE);
        } catch (ArithmeticException ex) {
            JOptionPane.showMessageDialog(this,
                    "Cannot divide by zero!",
                    "Arithmetic Error",
                    JOptionPane.ERROR_MESSAGE);
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this,
                    "An unexpected error occurred: " + ex.getMessage(),
                    "Error",
                    JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        new IntegerDivision();
    }
}""",
        "output": """[GUI opened: Integer Division]
When Num1=10, Num2=2 -> Result=5
When Num1=10, Num2=0 -> Error Dialog: Cannot divide by zero!
When Num1=abc, Num2=5 -> Error Dialog: Please enter valid integers!"""
    },
    {
        "id": "lab_add_05",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "MouseListenerDemo.java",
        "className": "MouseListenerDemo",
        "title": "Additional 5: Mouse Listener (5 Mouse Events)",
        "experimentNo": "Additional Program 5",
        "sourcePdf": "java r 1.pdf",
        "description": "AWT Frame demonstrating MouseListener interface handling mouseClicked, mousePressed, mouseReleased, mouseEntered, and mouseExited.",
        "tags": ["mouselistener", "awt", "event handling", "mouse events", "graphics"],
        "code": """package Java_Lab;

import java.awt.*;
import java.awt.event.*;

class myframe10 extends Frame implements MouseListener {
    String[] msg = new String[5];

    myframe10() {
        this.setSize(500, 500);
        this.setVisible(true);
        this.setBackground(Color.BLUE);
        this.addMouseListener(this);
    }

    public void mouseClicked(MouseEvent e) {
        msg[0] = "mouse clicked.................. (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    public void mousePressed(MouseEvent e) {
        msg[1] = "mouse pressed. ....(" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    public void mouseReleased(MouseEvent e) {
        msg[2] = "mouse released .... (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    public void mouseEntered(MouseEvent e) {
        msg[3] = "mouse entered. ... (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    public void mouseExited(MouseEvent e) {
        msg[4] = "mouse exited .... (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    public void paint(Graphics g) {
        int X = 50;
        int Y = 100;
        g.setColor(Color.WHITE);
        for (int i = 0; i < msg.length; i++) {
            if (msg[i] != null) {
                Y = Y + 50;
                g.drawString(msg[i], X, Y);
            }
        }
    }
}

public class MouseListenerDemo {
    public static void main(String[] args) {
        new myframe10();
    }
}""",
        "output": """[AWT Frame opened: Blue canvas recording mouse coordinate events]
mouse clicked.................. (145,210)
mouse pressed. ....(145,210)
mouse released .... (145,210)"""
    },
    {
        "id": "lab_add_06",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "MyApplet.java",
        "className": "MyApplet",
        "title": "Additional 6: My First Applet",
        "experimentNo": "Additional Program 6",
        "sourcePdf": "java r 1.pdf",
        "description": "Basic Applet lifecycle demonstrating paint() method with drawString greeting.",
        "tags": ["applet", "graphics", "drawstring", "awt"],
        "code": """package Java_Lab;

/*
<applet code="MyApplet" width=900 height=500>
</applet>
*/
import java.applet.Applet;
import java.awt.Graphics;

public class MyApplet extends Applet {
    public void paint(Graphics g) {
        g.drawString("Hello, this is my first Applet!", 50, 100);
    }
}""",
        "output": """[AppletViewer launched]
drawString at (50, 100): 'Hello, this is my first Applet!'"""
    },
    {
        "id": "lab_add_07",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "PhoneDirectory.java",
        "className": "PhoneDirectory",
        "title": "Additional 7: Two-Way Phone Directory (Hashtable)",
        "experimentNo": "Additional Program 7",
        "sourcePdf": "java r 1.pdf",
        "description": "Reads name and phone data from tab-separated file and provides fast bidirectional lookup using Hashtable.",
        "tags": ["hashtable", "file io", "collections", "lookup", "bufferedreader"],
        "code": """package Java_Lab;

import java.io.*;
import java.util.*;

public class PhoneDirectory {
    public static void main(String[] args) {
        Hashtable<String, String> nameToPhone = new Hashtable<>();
        Hashtable<String, String> phoneToName = new Hashtable<>();
        try {
            BufferedReader br = new BufferedReader(
                    new FileReader("D:\\\\Java Programs\\\\Core_Java\\\\src\\\\Phone.txt"));
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split("\\t");
                if (parts.length == 2) {
                    String name = parts[0].trim();
                    String phone = parts[1].trim();
                    nameToPhone.put(name, phone);
                    phoneToName.put(phone, name);
                }
            }
            br.close();

            Scanner sc = new Scanner(System.in);
            System.out.print("Enter a name or phone number to search: ");
            String input = sc.nextLine().trim();

            if (nameToPhone.containsKey(input)) {
                System.out.println("Phone Number: " + nameToPhone.get(input));
            } else if (phoneToName.containsKey(input)) {
                System.out.println("Name: " + phoneToName.get(input));
            } else {
                System.out.println("No record found for: " + input);
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error: File 'Phone.txt' not found.");
        } catch (IOException e) {
            System.out.println("Error reading from file.");
        }
    }
}""",
        "output": """Enter a name or phone number to search: Alice
Phone Number: 9876543210"""
    },
    {
        "id": "lab_add_08",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "SimpleCalculator.java",
        "className": "SimpleCalculator",
        "title": "Additional 8: Simple Calculator (Swing GUI)",
        "experimentNo": "Additional Program 8",
        "sourcePdf": "java r 1.pdf",
        "description": "Interactive Swing GUI Calculator with 4x4 keypad grid performing addition, subtraction, multiplication, and modulus.",
        "tags": ["calculator", "swing", "gridlayout", "actionlistener", "gui", "math"],
        "code": """package Java_Lab;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleCalculator extends JFrame implements ActionListener {
    JTextField display;
    double num1, num2, result;
    char operator;

    public SimpleCalculator() {
        setTitle("Simple Calculator");
        display = new JTextField();
        display.setEditable(false);
        add(display, BorderLayout.NORTH);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 4, 5, 5));

        String buttons[] = {
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", "%", "=", "C"
        };

        for (String text : buttons) {
            JButton b = new JButton(text);
            b.addActionListener(this);
            panel.add(b);
        }
        add(panel, BorderLayout.CENTER);
        setSize(300, 300);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        if (command.charAt(0) >= '0' && command.charAt(0) <= '9') {
            display.setText(display.getText() + command);
        } else if (command.equals("+") || command.equals("-") ||
                   command.equals("*") || command.equals("%")) {
            try {
                num1 = Double.parseDouble(display.getText());
                operator = command.charAt(0);
                display.setText("");
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("=")) {
            try {
                num2 = Double.parseDouble(display.getText());
                switch (operator) {
                    case '+': result = num1 + num2; break;
                    case '-': result = num1 - num2; break;
                    case '*': result = num1 * num2; break;
                    case '%':
                        if (num2 == 0)
                            throw new ArithmeticException("Divide by zero");
                        result = num1 % num2;
                        break;
                }
                display.setText(String.valueOf(result));
            } catch (ArithmeticException ex) {
                display.setText("Cannot divide by zero");
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("C")) {
            display.setText("");
            num1 = num2 = result = 0;
            operator = '\\0';
        }
    }

    public static void main(String[] args) {
        new SimpleCalculator();
    }
}""",
        "output": """[Swing Frame launched: Simple Calculator (300x300)]
Input: 25 * 4 = 100.0"""
    },
    {
        "id": "lab_add_09",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "TestApplet.java",
        "className": "TestApplet",
        "title": "Additional 9: Applet Lifecycle (init, start, paint)",
        "experimentNo": "Additional Program 9",
        "sourcePdf": "java r 1.pdf",
        "description": "Applet showing the execution sequence of init(), start(), and paint() lifecycle methods.",
        "tags": ["applet", "lifecycle", "init", "start", "paint", "awt"],
        "code": """package Java_Lab;

/*
<applet code="TestApplet.class" width=900 height=500>
</applet>
*/
import java.applet.Applet;
import java.awt.Graphics;

public class TestApplet extends Applet {
    String msg = " ";

    public void init() {
        msg = "init method begins";
        System.out.println(msg);
    }

    public void start() {
        msg += " -> Start method invoked";
        System.out.println(msg);
    }

    public void paint(Graphics g) {
        System.out.println(msg);
        msg += " -> paint method: WELCOME TO VBIT";
        g.drawString(msg, 50, 100);
        System.out.println(msg);
    }
}""",
        "output": """init method begins
init method begins -> Start method invoked
init method begins -> Start method invoked -> paint method: WELCOME TO VBIT"""
    },
    {
        "id": "lab_add_10",
        "category": "Lab Record (VBIT)",
        "project": "Java_Lab_Record",
        "package": "Java_Lab",
        "fileName": "TrafficLightSimulator.java",
        "className": "TrafficLightSimulator",
        "title": "Additional 10: Traffic Light Simulator (Swing GUI)",
        "experimentNo": "Additional Program 10",
        "sourcePdf": "java r 1.pdf",
        "description": "Swing GUI simulation of a traffic light using JRadioButton for Red, Yellow, Green with color-coded message display.",
        "tags": ["swing", "jradiobutton", "buttongroup", "traffic light", "gui", "event handling"],
        "code": """package Java_Lab;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TrafficLightSimulator extends JFrame implements ActionListener {
    JRadioButton redButton, yellowButton, greenButton;
    ButtonGroup group;
    JLabel messageLabel;

    public TrafficLightSimulator() {
        setTitle("Traffic Light Simulator");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        redButton = new JRadioButton("Red");
        yellowButton = new JRadioButton("Yellow");
        greenButton = new JRadioButton("Green");

        group = new ButtonGroup();
        group.add(redButton);
        group.add(yellowButton);
        group.add(greenButton);

        redButton.addActionListener(this);
        yellowButton.addActionListener(this);
        greenButton.addActionListener(this);

        messageLabel = new JLabel("");
        messageLabel.setFont(new Font("Arial", Font.BOLD, 24));

        add(messageLabel);
        add(redButton);
        add(yellowButton);
        add(greenButton);

        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (redButton.isSelected()) {
            messageLabel.setText("STOP");
            messageLabel.setForeground(Color.RED);
        } else if (yellowButton.isSelected()) {
            messageLabel.setText("READY");
            messageLabel.setForeground(Color.ORANGE);
        } else if (greenButton.isSelected()) {
            messageLabel.setText("GO");
            messageLabel.setForeground(Color.GREEN);
        }
    }

    public static void main(String[] args) {
        new TrafficLightSimulator();
    }
}""",
        "output": """[Swing Frame launched: Traffic Light Simulator (400x300)]
Click Red -> "STOP" (Red text)
Click Yellow -> "READY" (Orange text)
Click Green -> "GO" (Green text)"""
    },

    # =========================================================================
    # GROUP 2: Exam Ready Programs (jajajajaj.pdf)
    # =========================================================================
    {
        "id": "exam_prog_01",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "ShapeDemo.java",
        "className": "ShapeDemo",
        "title": "1. Abstract Class – Shape, Rectangle, Triangle and Circle",
        "experimentNo": "Question 1",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Abstract class Shape with abstract printArea() method, implemented by Rectangle, Triangle, and Circle.",
        "tags": ["abstract class", "inheritance", "polymorphism", "shapes", "geometry", "area"],
        "code": """abstract class Shape {
    int a, b;
    abstract void printArea();
}

class Rectangle extends Shape {
    Rectangle(int length, int breadth) {
        a = length;
        b = breadth;
    }

    void printArea() {
        System.out.println("Area of Rectangle = " + (a * b));
    }
}

class Triangle extends Shape {
    Triangle(int base, int height) {
        a = base;
        b = height;
    }

    void printArea() {
        System.out.println("Area of Triangle = " + (0.5 * a * b));
    }
}

class Circle extends Shape {
    Circle(int radius) {
        a = radius;
    }

    void printArea() {
        System.out.println("Area of Circle = " + (Math.PI * a * a));
    }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(10, 5);
        Triangle t = new Triangle(10, 5);
        Circle c = new Circle(7);

        r.printArea();
        t.printArea();
        c.printArea();
    }
}""",
        "output": """Area of Rectangle = 50
Area of Triangle = 25.0
Area of Circle = 153.93804002589985"""
    },
    {
        "id": "exam_prog_02",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "MultilevelDemo.java",
        "className": "MultilevelDemo",
        "title": "2. Multilevel Inheritance",
        "experimentNo": "Question 2",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate multilevel inheritance hierarchy: GrandFather -> Father -> Son.",
        "tags": ["multilevel inheritance", "inheritance", "extends", "oops"],
        "code": """class GrandFather {
    void showGrandFather() {
        System.out.println("Grandfather class");
    }
}

class Father extends GrandFather {
    void showFather() {
        System.out.println("Father class");
    }
}

class Son extends Father {
    void showSon() {
        System.out.println("Son class");
    }
}

public class MultilevelDemo {
    public static void main(String[] args) {
        Son s = new Son();
        s.showGrandFather();
        s.showFather();
        s.showSon();
    }
}""",
        "output": """Grandfather class
Father class
Son class"""
    },
    {
        "id": "exam_prog_03",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "FinalDemo.java",
        "className": "FinalDemo",
        "title": "3. Final Keyword",
        "experimentNo": "Question 3",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate final variable (cannot be changed) and final method (cannot be overridden).",
        "tags": ["final", "keyword", "constant", "methods", "immutable"],
        "code": """public class FinalDemo {
    final int VALUE = 100;

    final void display() {
        System.out.println("This is a final method.");
        System.out.println("Value = " + VALUE);
    }

    public static void main(String[] args) {
        FinalDemo obj = new FinalDemo();
        obj.display();
    }
}""",
        "output": """This is a final method.
Value = 100"""
    },
    {
        "id": "exam_prog_04",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.utils",
        "fileName": "Palindrome.java",
        "className": "Palindrome",
        "title": "4. StringBuffer Mutability – Palindrome",
        "experimentNo": "Question 4",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Check palindrome string using StringBuffer's reverse() method and equals comparison.",
        "tags": ["stringbuffer", "palindrome", "mutability", "scanner", "string reverse"],
        "code": """import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        StringBuffer sb = new StringBuffer(str);
        String reverse = sb.reverse().toString();

        if (str.equals(reverse))
            System.out.println("The string is a palindrome.");
        else
            System.out.println("The string is not a palindrome.");
        sc.close();
    }
}""",
        "output": """Enter a string: radar
The string is a palindrome."""
    },
    {
        "id": "exam_prog_05",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "AbstractDemo.java",
        "className": "AbstractDemo",
        "title": "5. Abstract Class and Abstract Methods",
        "experimentNo": "Question 5",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate abstract class Animal with abstract method sound() and concrete method eat().",
        "tags": ["abstract", "abstract methods", "animal", "polymorphism", "oops"],
        "code": """abstract class Animal {
    abstract void sound();

    void eat() {
        System.out.println("Animal eats food");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks");
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.sound();
        d.eat();
    }
}""",
        "output": """Dog barks
Animal eats food"""
    },
    {
        "id": "exam_prog_06",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "SuperDemo.java",
        "className": "SuperDemo",
        "title": "6. Super Keyword",
        "experimentNo": "Question 6",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate super keyword to access parent class instance variable and parent class method.",
        "tags": ["super", "keyword", "parent child", "inheritance", "variable hiding"],
        "code": """class Parent {
    int number = 100;

    void display() {
        System.out.println("Parent class method");
    }
}

class Child extends Parent {
    int number = 200;

    void display() {
        System.out.println("Child class method");
    }

    void show() {
        System.out.println("Parent variable = " + super.number);
        super.display();
        System.out.println("Child variable = " + number);
    }
}

public class SuperDemo {
    public static void main(String[] args) {
        Child c = new Child();
        c.show();
    }
}""",
        "output": """Parent variable = 100
Parent class method
Child variable = 200"""
    },
    {
        "id": "exam_prog_07",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.utils",
        "fileName": "PackageDemo.java",
        "className": "PackageDemo",
        "title": "7. User-Defined Package – sample",
        "experimentNo": "Question 7",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate creating user package sample with Test class and importing it into PackageDemo.",
        "tags": ["package", "sample", "import", "user defined", "modules"],
        "code": """// File 1: sample/Test.java
// package sample;
// public class Test {
//     public void display() {
//         System.out.println("This is a user-defined package.");
//     }
// }

// File 2: PackageDemo.java
class Test {
    public void display() {
        System.out.println("This is a user-defined package.");
    }
}

public class PackageDemo {
    public static void main(String[] args) {
        Test obj = new Test();
        obj.display();
    }
}""",
        "output": """This is a user-defined package."""
    },
    {
        "id": "exam_prog_08",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "InterfaceDemo.java",
        "className": "InterfaceDemo",
        "title": "8. Interface",
        "experimentNo": "Question 8",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate defining an interface Animal with sound() method and implementing it in class Dog.",
        "tags": ["interface", "implements", "animal", "abstraction", "oops"],
        "code": """interface Animal {
    void sound();
}

class Dog implements Animal {
    public void sound() {
        System.out.println("Dog barks");
    }
}

public class InterfaceDemo {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.sound();
    }
}""",
        "output": """Dog barks"""
    },
    {
        "id": "exam_prog_09",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.exceptions",
        "fileName": "UserExceptionDemo.java",
        "className": "UserExceptionDemo",
        "title": "9. User-Defined Exception Using throw",
        "experimentNo": "Question 9",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Create custom AgeException extending Exception and explicitly throw it using 'throw' keyword.",
        "tags": ["user defined exception", "throw", "custom exception", "exception handling", "validation"],
        "code": """class AgeException extends Exception {
    AgeException(String message) {
        super(message);
    }
}

public class UserExceptionDemo {
    public static void main(String[] args) {
        int age = 15;
        try {
            if (age < 18)
                throw new AgeException("Age must be 18 or above");

            System.out.println("Eligible");
        } catch (AgeException e) {
            System.out.println(e.getMessage());
        }
    }
}""",
        "output": """Age must be 18 or above"""
    },
    {
        "id": "exam_prog_10",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "MultipleInheritanceDemo.java",
        "className": "MultipleInheritanceDemo",
        "title": "10. Multiple Inheritance Using Interface",
        "experimentNo": "Question 10",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Java does not support multiple inheritance with classes, but supports it through interfaces (Father and Mother implemented by Child).",
        "tags": ["multiple inheritance", "interface", "father mother child", "implements"],
        "code": """interface Father {
    void showFather();
}

interface Mother {
    void showMother();
}

class Child implements Father, Mother {
    public void showFather() {
        System.out.println("Father interface");
    }

    public void showMother() {
        System.out.println("Mother interface");
    }
}

public class MultipleInheritanceDemo {
    public static void main(String[] args) {
        Child c = new Child();
        c.showFather();
        c.showMother();
    }
}""",
        "output": """Father interface
Mother interface"""
    },
    {
        "id": "exam_prog_11",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "HierarchicalDemo.java",
        "className": "HierarchicalDemo",
        "title": "11. Hierarchical Inheritance",
        "experimentNo": "Question 11",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate Hierarchical Inheritance where multiple child classes (Dog, Cat) inherit from single parent (Animal).",
        "tags": ["hierarchical inheritance", "inheritance", "animal dog cat", "oops"],
        "code": """class Animal {
    void eat() {
        System.out.println("Animal eats");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("Cat meows");
    }
}

public class HierarchicalDemo {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.bark();

        Cat c = new Cat();
        c.eat();
        c.meow();
    }
}""",
        "output": """Animal eats
Dog barks
Animal eats
Cat meows"""
    },
    {
        "id": "exam_prog_12",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.exceptions",
        "fileName": "ThrowsDemo.java",
        "className": "ThrowsDemo",
        "title": "12. Exception Handling Using throws",
        "experimentNo": "Question 12",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate throws keyword to declare that divide() method may throw an ArithmeticException.",
        "tags": ["throws", "exception declaration", "arithmeticexception", "try catch"],
        "code": """public class ThrowsDemo {
    static void divide() throws ArithmeticException {
        int a = 10;
        int b = 0;
        System.out.println(a / b);
    }

    public static void main(String[] args) {
        try {
            divide();
        } catch (ArithmeticException e) {
            System.out.println("Exception: " + e);
        }
    }
}""",
        "output": """Exception: java.lang.ArithmeticException: / by zero"""
    },
    {
        "id": "exam_prog_13",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "SingleInheritanceDemo.java",
        "className": "SingleInheritanceDemo",
        "title": "13. Single Inheritance",
        "experimentNo": "Question 13",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate Single Inheritance: Dog extends Animal.",
        "tags": ["single inheritance", "inheritance", "animal dog", "extends", "oops"],
        "code": """class Animal {
    void eat() {
        System.out.println("Animal eats food");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks");
    }
}

public class SingleInheritanceDemo {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.bark();
    }
}""",
        "output": """Animal eats food
Dog barks"""
    },
    {
        "id": "exam_prog_14",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.exceptions",
        "fileName": "MultipleCatchDemo.java",
        "className": "MultipleCatchDemo",
        "title": "14. Exception Handling – Multiple Catch Blocks",
        "experimentNo": "Question 14",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate handling multiple exceptions (ArrayIndexOutOfBoundsException, ArithmeticException, Exception) in order of specificity.",
        "tags": ["multiple catch", "exception handling", "arrayindexoutofboundsexception", "arithmeticexception"],
        "code": """public class MultipleCatchDemo {
    public static void main(String[] args) {
        try {
            int a[] = {10, 20, 30};
            System.out.println(a[5]);
            int x = 10 / 0;
            System.out.println(x);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index is out of bounds.");
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        } catch (Exception e) {
            System.out.println("Some other exception occurred.");
        }
    }
}""",
        "output": """Array index is out of bounds."""
    },
    {
        "id": "exam_prog_15",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.utils",
        "fileName": "Armstrong.java",
        "className": "Armstrong",
        "title": "15. Armstrong Number Using if-else and for Loop",
        "experimentNo": "Question 15",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Determine if a given number is an Armstrong number (sum of cubes of digits equals the original number) using for loop and if-else.",
        "tags": ["armstrong", "for loop", "if else", "scanner", "math", "algorithms"],
        "code": """import java.util.Scanner;

public class Armstrong {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int original = n;
        int sum = 0;

        for (; n != 0; n = n / 10) {
            int digit = n % 10;
            sum = sum + digit * digit * digit;
        }

        if (sum == original)
            System.out.println(original + " is an Armstrong number.");
        else
            System.out.println(original + " is not an Armstrong number.");
        sc.close();
    }
}""",
        "output": """Enter a number: 153
153 is an Armstrong number."""
    },
    {
        "id": "exam_prog_16",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.oop",
        "fileName": "VehicleDemo.java",
        "className": "VehicleDemo",
        "title": "16. Vehicle Interface",
        "experimentNo": "Question 16",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Vehicle interface with start() and stop() methods implemented by Car and Bike classes.",
        "tags": ["interface", "vehicle", "car", "bike", "polymorphism", "oops"],
        "code": """interface Vehicle {
    void start();
    void stop();
}

class Car implements Vehicle {
    public void start() {
        System.out.println("Car starts");
    }

    public void stop() {
        System.out.println("Car stops");
    }
}

class Bike implements Vehicle {
    public void start() {
        System.out.println("Bike starts");
    }

    public void stop() {
        System.out.println("Bike stops");
    }
}

public class VehicleDemo {
    public static void main(String[] args) {
        Car c = new Car();
        c.start();
        c.stop();

        Bike b = new Bike();
        b.start();
        b.stop();
    }
}""",
        "output": """Car starts
Car stops
Bike starts
Bike stops"""
    },
    {
        "id": "exam_prog_17",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.exceptions",
        "fileName": "FinallyDemo.java",
        "className": "FinallyDemo",
        "title": "17. Exception Handling Using try, catch and finally",
        "experimentNo": "Question 17",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Demonstrate that the finally block always executes regardless of whether an exception is caught or handled.",
        "tags": ["try catch finally", "finally", "exception handling", "cleanup", "guaranteed execution"],
        "code": """public class FinallyDemo {
    public static void main(String[] args) {
        try {
            int a = 10;
            int b = 0;
            System.out.println(a / b);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        } finally {
            System.out.println("Finally block is always executed.");
        }
    }
}""",
        "output": """Cannot divide by zero.
Finally block is always executed."""
    },
    {
        "id": "exam_prog_18",
        "category": "Exam Ready Programs",
        "project": "Exam_Ready_Programs",
        "package": "exam.revision",
        "fileName": "QuickExamRevision.java",
        "className": "QuickExamRevision",
        "title": "Quick Exam Revision – Core Java Concepts & Keywords Matrix",
        "experimentNo": "Revision Summary",
        "sourcePdf": "jajajajaj.pdf",
        "description": "Complete reference matrix of core Java topics and their respective main keywords/concepts from the exam guide.",
        "tags": ["revision", "cheat sheet", "matrix", "keywords", "summary", "exam guide"],
        "code": """/**
 * QUICK EXAM REVISION SUMMARY
 * -------------------------------------------------------------------------
 * Topic                     | Main keyword/concept
 * -------------------------------------------------------------------------
 * Abstract class            | abstract (cannot be instantiated, subclasses provide body)
 * Single inheritance        | extends (one child class inherits one parent class)
 * Multilevel inheritance   | Multiple extends levels (GrandFather -> Father -> Son)
 * Hierarchical inheritance  | One parent, multiple children (Animal -> Dog, Cat)
 * Multiple inheritance      | interface (classes cannot multi-inherit, interfaces can)
 * Interface                 | implements (defines contract with abstract methods)
 * Super keyword             | super (refers to immediate parent class variable/method/ctor)
 * Final keyword             | final (constants, non-overridable methods, unextendable class)
 * User-defined exception    | throw (throw custom instance extending java.lang.Exception)
 * Exception declaration     | throws (declares list of checked exceptions method may throw)
 * Exception handling        | try-catch (encloses risky code and catches specific exceptions)
 * Always-executed block     | finally (always executes for resource cleanup)
 * StringBuffer              | Mutable string (supports in-place reverse, append, insert)
 * Package                   | package, import (namespace partitioning and modularity)
 * -------------------------------------------------------------------------
 */
public class QuickExamRevision {
    public static void main(String[] args) {
        String[][] cheatSheet = {
            {"Abstract class", "abstract"},
            {"Single inheritance", "extends"},
            {"Multilevel inheritance", "Multiple extends levels"},
            {"Hierarchical inheritance", "One parent, multiple children"},
            {"Multiple inheritance", "interface"},
            {"Interface", "implements"},
            {"Super keyword", "super"},
            {"Final keyword", "final"},
            {"User-defined exception", "throw"},
            {"Exception declaration", "throws"},
            {"Exception handling", "try-catch"},
            {"Always-executed block", "finally"},
            {"StringBuffer", "Mutable string"},
            {"Package", "package, import"}
        };

        System.out.println(String.format("%-25s | %s", "Topic", "Main keyword/concept"));
        System.out.println("-----------------------------------------------------------------");
        for (String[] row : cheatSheet) {
            System.out.println(String.format("%-25s | %s", row[0], row[1]));
        }
    }
}""",
        "output": """Topic                     | Main keyword/concept
-----------------------------------------------------------------
Abstract class            | abstract
Single inheritance        | extends
Multilevel inheritance    | Multiple extends levels
Hierarchical inheritance  | One parent, multiple children
Multiple inheritance      | interface
Interface                 | implements
Super keyword             | super
Final keyword             | final
User-defined exception    | throw
Exception declaration     | throws
Exception handling        | try-catch
Always-executed block     | finally
StringBuffer              | Mutable string
Package                   | package, import"""
    },

    # =========================================================================
    # GROUP 3: Complete JDBC CRUD Operations (JDBC.pdf)
    # =========================================================================
    {
        "id": "jdbc_crud_01",
        "category": "JDBC Operations",
        "project": "JDBC_Database_Connectivity",
        "package": "com.jdbc.crud",
        "fileName": "CreateTable.java",
        "className": "CreateTable",
        "title": "CREATE – Create Table Operation",
        "experimentNo": "JDBC CRUD 1",
        "sourcePdf": "JDBC.pdf",
        "description": "Establish connection using DriverManager and execute CREATE TABLE statement using Statement.executeUpdate().",
        "tags": ["jdbc", "sql", "create table", "drivermanager", "statement", "mysql"],
        "code": """import java.sql.*;

public class CreateTable {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "password");
        Statement st = con.createStatement();
        st.executeUpdate(
            "CREATE TABLE student (id INT, name VARCHAR(30))");
        System.out.println("Table created");
        con.close();
    }
}""",
        "output": """Table created"""
    },
    {
        "id": "jdbc_crud_02",
        "category": "JDBC Operations",
        "project": "JDBC_Database_Connectivity",
        "package": "com.jdbc.crud",
        "fileName": "InsertData.java",
        "className": "InsertData",
        "title": "INSERT – Insert Record Operation",
        "experimentNo": "JDBC CRUD 2",
        "sourcePdf": "JDBC.pdf",
        "description": "Execute INSERT INTO SQL statement to insert a new student record into the database table.",
        "tags": ["jdbc", "insert", "sql", "crud", "statement", "database"],
        "code": """import java.sql.*;

public class InsertData {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "password");
        Statement st = con.createStatement();
        st.executeUpdate(
            "INSERT INTO student VALUES (1, 'Ravi')");
        System.out.println("Record inserted");
        con.close();
    }
}""",
        "output": """Record inserted"""
    },
    {
        "id": "jdbc_crud_03",
        "category": "JDBC Operations",
        "project": "JDBC_Database_Connectivity",
        "package": "com.jdbc.crud",
        "fileName": "SelectData.java",
        "className": "SelectData",
        "title": "SELECT – Read / Query Data Operation",
        "experimentNo": "JDBC CRUD 3",
        "sourcePdf": "JDBC.pdf",
        "description": "Execute SELECT * query and iterate through the ResultSet to print student id and name.",
        "tags": ["jdbc", "select", "resultset", "query", "sql", "crud"],
        "code": """import java.sql.*;

public class SelectData {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "password");
        Statement st = con.createStatement();
        ResultSet rs = st.executeQuery("SELECT * FROM student");
        while (rs.next()) {
            System.out.println(
                rs.getInt("id") + " " +
                rs.getString("name"));
        }
        con.close();
    }
}""",
        "output": """1 Ravi"""
    },
    {
        "id": "jdbc_crud_04",
        "category": "JDBC Operations",
        "project": "JDBC_Database_Connectivity",
        "package": "com.jdbc.crud",
        "fileName": "UpdateData.java",
        "className": "UpdateData",
        "title": "UPDATE – Update Record Operation",
        "experimentNo": "JDBC CRUD 4",
        "sourcePdf": "JDBC.pdf",
        "description": "Execute UPDATE SQL query to update student record where id = 1, checking affected row count.",
        "tags": ["jdbc", "update", "executeupdate", "rows affected", "sql", "crud"],
        "code": """import java.sql.*;

public class UpdateData {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "password");
        Statement st = con.createStatement();
        int rows = st.executeUpdate(
            "UPDATE student SET name = 'Surya' WHERE id = 1");
        if (rows > 0) {
            System.out.println("Record updated successfully!");
        } else {
            System.out.println("No record found.");
        }
        st.close();
        con.close();
    }
}""",
        "output": """Record updated successfully!"""
    },
    {
        "id": "jdbc_crud_05",
        "category": "JDBC Operations",
        "project": "JDBC_Database_Connectivity",
        "package": "com.jdbc.crud",
        "fileName": "DeleteData.java",
        "className": "DeleteData",
        "title": "DELETE – Delete Record Operation (PreparedStatement)",
        "experimentNo": "JDBC CRUD 5",
        "sourcePdf": "JDBC.pdf",
        "description": "Prompt user for student ID and safely delete the record using parameterized PreparedStatement.",
        "tags": ["jdbc", "delete", "preparedstatement", "parameterized query", "scanner", "sql"],
        "code": """import java.sql.*;
import java.util.Scanner;

public class DeleteData {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "password");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter student ID to delete: ");
        int id = sc.nextInt();
        PreparedStatement ps = con.prepareStatement(
            "DELETE FROM student WHERE id = ?");
        ps.setInt(1, id);
        int rows = ps.executeUpdate();
        if (rows > 0) {
            System.out.println("Student deleted successfully.");
        } else {
            System.out.println("Student ID not found.");
        }
        ps.close();
        con.close();
        sc.close();
    }
}""",
        "output": """Enter student ID to delete: 1
Student deleted successfully."""
    }
]

# Write to programs_data.js and programs_data.json
with open('programs_data.js', 'w', encoding='utf-8') as f:
    f.write('// Auto-generated Java Programs Database\n')
    f.write('window.JAVA_PROGRAMS = ')
    json.dump(programs, f, indent=2)
    f.write(';\n')

with open('programs_data.json', 'w', encoding='utf-8') as f:
    json.dump(programs, f, indent=2)

print(f"Successfully generated {len(programs)} programs into programs_data.js and programs_data.json!")

