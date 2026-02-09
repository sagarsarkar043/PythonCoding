# Sample Markdown File

This is a plain text file formatted using **Markdown** syntax. Markdown is a lightweight markup language used for creating formatted text using a plain-text editor.

---

## Headers

You can create headers using hash marks (`#`):

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

## Emphasis

*   *Italic text* or _italic text_ (single asterisks or underscores).
*   **Bold text** or __bold text__ (double asterisks or underscores).
*   ***Bold and italic text*** (triple asterisks).
*   ~Strikethrough text~ (two tildes, not standard Markdown but supported by many flavors like GitHub Flavored Markdown).

## Lists

### Unordered List

Use asterisks (`*`), hyphens (`-`), or plus signs (`+`).

*   Item 1
*   Item 2
    *   Nested item A
    *   Nested item B
*   Item 3

### Ordered List

Use numbers followed by a period.

1.  First item
2.  Second item
3.  Third item
    1.  Nested ordered item
    2.  Another nested item

## Links

You can create inline links:
[Visit the Markdown Guide](https://www.markdownguide.org).

Or use reference-style links for cleaner text flow:
[The best search engine][google].

[google]: https://www.google.com "Google Homepage"

## Images

Images are similar to links but start with an exclamation mark (`!`).

![Markdown Logo](https://markdownlivepreview.com)

## Blockquotes

Use the greater-than sign (`>`) to quote text.

> Dorothy followed her through many of the beautiful rooms in her castle.
> 
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

## Code Blocks

Use single backticks (`` ` ``) for `inline code` or triple backticks (```` ``` ````) for fenced code blocks with optional syntax highlighting.

````markdown
```javascript
// Example JavaScript code
function helloWorld() {
  console.log("Hello, World!");
}
helloWorld();
