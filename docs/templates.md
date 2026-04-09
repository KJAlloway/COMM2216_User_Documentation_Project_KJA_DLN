# Configuring Code Templates

## Overview

IntelliJ IDEA generates boilerplate Java methods — `equals()`, `hashCode()`,
and `toString()` — using [Velocity templates](glossary.md#velocity-template)
when you use the **Generate** menu. The default templates do not match COMP 2522
style requirements. This section walks you through replacing them so that every
time you generate these methods, the output is already compliant.

This also covers configuring the [Javadoc](glossary.md#javadoc) plugin's class-level
comment template so that generated class headers include the required
`@author` and `@version` tags automatically.

By the end of this section, generating `equals()`, `hashCode()`, `toString()`,
and class-level Javadoc from the Generate menu will produce COMP 2522-compliant
output without any manual edits.

!!! note
    These templates are stored globally in your IDE settings and apply to
    every project you open. You only need to configure them once.

!!! warning
    You do not need an open project to configure templates. These steps
    can be completed from the IntelliJ IDEA welcome screen by navigating
    to **Customize > All Settings**.

## Configuring the toString Template

The default `toString()` template uses string [concatenation](glossary.md#string)
with `+`. COMP 2522 requires [StringBuilder](glossary.md#string) for all string
construction. The template below generates a compliant `toString()` method
automatically.

1. Open any Java class in the editor and press ++alt+insert++ to open
   the **Generate** menu.

    Alternatively, from the welcome screen navigate to
    **Customize > All Settings > Editor > File and Code Templates**.

2. Select **toString()** from the Generate menu.

    At this point, the **Generate toString()** dialog opens showing
    your class fields.

3. Click the **...** button beside the **Template** dropdown in the
   top-right area of the dialog.

    At this point, the **toString() Generation Settings** dialog opens.

4. Click the **Templates** tab.

5. Select the existing template and click **Edit**, or click **Add** to
   create a new one named `COMP 2522 toString`.

6. Replace the entire template contents with the following:

    ```
    public java.lang.String toString() {
    final java.lang.StringBuilder sb;
    sb = new java.lang.StringBuilder("$classname{");
    #if ($parentClassName != "Object")
    sb.append("super=").append(super.toString());
        #set ($i = 1)
    #else
        #set ($i = 0)
    #end
    #foreach ($member in $members)
        #if ($i == 0)
        sb.append("##
        #else
        sb.append(", ##
        #end
        #if ($member.string)
            $member.name='")##
        #else
            $member.name=")##
        #end
        #if ($member.primitiveArray || $member.objectArray)
        .append(java.util.Arrays.toString($member.name));
        #elseif ($member.string)
        .append($member.accessor).append('\'');
        #else
        .append($member.accessor);
        #end
        #set ($i = $i + 1)
    #end
    sb.append('}');
    return sb.toString();
    }
    ```

7. Click **OK** to save the template.

8. Back in the toString() Settings dialog, select your updated template
   from the **Template** dropdown to make it active.

9. Click **OK** to close the settings dialog.

10. Click **OK** in the Generate toString() dialog to generate the method
    for your current class and verify the output matches the COMP 2522
    pattern.

!!! tip
    Press ++ctrl+z++ to undo the generated method if the output is not
    what you expected, and revisit the template.

## Configuring the equals and hashCode Templates

The default `equals()` template uses `instanceof` for type checking, which
is prohibited in COMP 2522. The templates below use `getClass()` instead,
and generate a compliant `hashCode()` alongside it.

1. Open any Java class in the editor and press ++alt+insert++ to open
   the **Generate** menu.

2. Select **equals() and hashCode()** from the Generate menu.

    At this point, the **Generate equals() and hashCode()** wizard opens.

3. Click the **...** button beside the **Template** dropdown.

    At this point, the template editor opens.

4. Select the existing equals template and click **Edit**, or click
   **Add** to create a new one named `COMP 2522 equals`.

5. Replace the entire equals template contents with the following:

    ```
    #parse("equalsHelper.vm")
    public boolean equals(##
    #if ($settings.generateFinalParameters)
    final ##
    #end
    Object $paramName){
    #addEqualsPrologue()
    #addClassInstance()
    return ##
    #set($i = 0)
    #if($superHasEquals)
    super.equals($paramName) ##
        #set($i = 1)
    #end
    #foreach($field in $fields)
        #if ($i > 0)
        && ##
        #end
        #set($i = $i + 1)
        #if ($field.primitive)
            #if ($field.double || $field.float)
                #addDoubleFieldComparisonConditionDirect($field) ##
            #else
                #addPrimitiveFieldComparisonConditionDirect($field) ##
            #end
        #elseif ($field.enum)
            #addPrimitiveFieldComparisonConditionDirect($field) ##
        #elseif ($field.array)
        java.util.Objects.deepEquals($field.accessor, ${classInstanceName}.$field.accessor)##
        #else
        java.util.Objects.equals($field.accessor, ${classInstanceName}.$field.accessor)##
        #end
    #end
    ;
    }
    ```

6. Click **OK** to save the equals template.

7. Now select the hashCode template and click **Edit**, or add a new one
   named `COMP 2522 hashCode`.

8. Replace the entire hashCode template contents with the following:

    ```
    public int hashCode() {
    #if (!$superHasHashCode && $fields.size()==1)
        #if (!$fields[0].array)
        return java.util.Objects.hashCode($fields[0].accessor);
        #elseif ($fields[0].nestedArray)
        return java.util.Arrays.deepHashCode($fields[0].accessor);
        #else
        return java.util.Arrays.hashCode($fields[0].accessor);
        #end
    #else
    return java.util.Objects.hash(##
        #set($i = 0)
        #if($superHasHashCode)
        super.hashCode() ##
            #set($i = 1)
        #end
        #foreach($field in $fields)
            #if ($i > 0)
            , ##
            #end
            #if(!$field.array)
                $field.accessor ##
            #elseif ($field.nestedArray)
            java.util.Arrays.deepHashCode($field.accessor)##
            #else
            java.util.Arrays.hashCode($field.accessor)##
            #end
            #set($i = $i + 1)
        #end
    );
    #end
    }
    ```

9. Click **OK** to save the hashCode template.

10. Back in the equals() and hashCode() wizard, select your updated
    templates from the dropdowns and click **Next** to select the fields
    to include.

11. Click **Finish** to generate the methods.

!!! tip
    After generating, verify that the `equals()` method uses
    `getClass() != object.getClass()` rather than `instanceof`.
    If `instanceof` appears, press ++ctrl+z++ to undo and confirm
    your template is selected in the dropdown.

## Configuring the Javadoc Class Template

The JavaDoc plugin generates class-level [Javadoc](glossary.md#javadoc) comments
using its own template system. The default template does not include
`@author` or `@version` tags, which are required by the COMP 2522 Style Guide
for all classes.

1. Open **File > Settings** (++ctrl+alt+s++).

2. Navigate to **Tools > JavaDoc** in the left panel.

3. Click the **Templates** tab.

4. Select **Class level** from the template list.

    At this point, you will see four template fields for the class-level
    comment. Replace all four with the following:

    ```
    /**
     * @author Your Name
     * @version X.X
     */
    ```

5. Click **Apply** then **OK**.

    At this point, any class-level Javadoc generated by the plugin will
    include the `@author` and `@version` tags ready for you to fill in.

!!! note
    Replace `Your Name` with your actual name and `X.X` with your
    version number (typically `1.0` for a new class) each time you
    generate. The template provides the structure — the values are
    yours to fill in.

## Conclusion

Your code generation templates are now configured to produce COMP 2522-compliant
output automatically. Every `equals()`, `hashCode()`, `toString()`, and
class-level Javadoc comment generated from the **Generate** menu will match
your instructor's style requirements from the first keystroke.
