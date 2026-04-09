# Glossary

| Term | Definition |
|---|---|
| **Annotation** | A metadata tag in Java code beginning with `@`, used to provide information to the compiler or IDE. Common examples include `@Override`, `@author`, and `@param` |
| **Build tool** | Software that automates compiling, testing, and packaging Java code. IntelliJ IDEA integrates with the two most common build tools: Maven and Gradle |
| **Caret** | The blinking cursor in the editor that marks your current position in the file. IntelliJ IDEA supports multiple carets simultaneously for editing several locations at once |
| **Checkstyle** | A static analysis tool that checks Java source code against a defined ruleset. In CST courses, your instructor uses a Checkstyle XML configuration file to grade code style compliance |
| **Code inspection** | An automated analysis rule that IntelliJ IDEA applies to your code as you type, flagging potential errors, warnings, and style violations without requiring compilation |
| **Code style** | A set of formatting and structural rules that determine how code is written — indentation, line length, naming conventions, and so on |
| **IDE** | Integrated Development Environment — a software application that combines a code editor, compiler or interpreter, debugger, and other tools into a single interface |
| **Indexing** | A background process IntelliJ IDEA runs when opening a project, scanning and cataloguing all files so features like Search Everywhere and Go to Declaration work correctly. Indicated by a progress bar in the bottom-right corner of the IDE |
| **Javadoc** | Java's standard documentation comment format, written using `/** */` blocks above classes, methods, and fields. Javadoc comments support tags like `@param`, `@return`, `@throws`, `@author`, and `@version` |
| **JDK** | Java Development Kit — a software package that includes the Java compiler, runtime environment, and standard libraries required to write and run Java programs |
| **JetBrains account** | An online account used to manage JetBrains licences and sync IDE settings across multiple devices |
| **Keymap** | A complete set of keyboard shortcut assignments for IDE actions. IntelliJ IDEA includes predefined keymaps and allows you to create and import custom ones |
| **Lint / linting** | An informal term for the process of running static analysis tools — like Checkstyle or IntelliJ inspections — to catch code style and quality issues automatically |
| **Magic number** | A numeric literal used directly in code instead of being assigned to a named constant. For example, writing `if (score > 100)` instead of defining `static final int MAX_SCORE = 100` and writing `if (score > MAX_SCORE)` |
| **Plugin** | An optional add-on that extends IntelliJ IDEA's built-in functionality with new features or language support |
| **Profile (inspection)** | A saved collection of inspection settings that can be exported, shared, and imported between IDE installations |
| **Project tool window** | The panel on the left side of the IntelliJ IDEA interface that displays your project's file and folder structure |
| **Refactoring** | Restructuring existing code to improve its design or readability without changing its external behaviour. Common refactoring operations include renaming, extracting methods, and introducing variables |
| **Run configuration** | A saved set of parameters that tells IntelliJ IDEA how to run or debug your program — including which class to launch, what arguments to pass, and which JDK to use |
| **Scope (IDE settings)** | Whether a setting applies to a single project only, or globally to every project you open. Settings stored at the IDE level apply everywhere; settings stored at the project level apply only to that project |
| **Settings sync** | An IntelliJ IDEA feature that uploads your IDE configuration — including keymaps, plugins, and code style settings — to your JetBrains account so they are available on any device you log into |
| **Severity** | The level of importance assigned to an inspection finding: Error, Warning, Weak Warning, or Typo |
| **Static analysis** | The process of examining source code without executing it, to identify potential errors, style violations, or quality issues. Both IntelliJ inspections and Checkstyle are static analysis tools |
| **String** | A sequence of characters treated as text in Java, represented by the `String` class. Strings are enclosed in double quotes: `"Hello, world!"` |
| **Stub** | A generated code skeleton with placeholder content that you fill in. The JavaDoc plugin generates Javadoc stubs — it inserts the comment structure with empty descriptions for you to complete |
| **Tool window** | A panel docked to the edge of the IntelliJ IDEA interface that provides access to a specific feature or view. Examples include the Project tool window, the Checkstyle tool window, and the Terminal |
| **UML** | Unified Modelling Language — a standardised notation for creating diagrams that represent the structure and behaviour of software systems |
| **Velocity template** | The templating language IntelliJ IDEA uses internally for code generation. When you use the Generate menu to create `equals()`, `hashCode()`, or `toString()` methods, IntelliJ fills in the code using a Velocity template that you can customize |
| **Wildcard import** | An import statement that uses `*` to import all classes from a package at once, for example `import java.util.*`. Wildcard imports are prohibited in COMP 2522 because they obscure which classes your code actually depends on |
