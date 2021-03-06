# NFA to DFA Converter

This application gets NFA data from a `txt` file. File structure can be found [below](#NFA-File-Structure). Application GUI is simple to use. Click on "import" to select NFA file and click on "convert" to get the output. Further updates may include;

- A canvas for the program to draw the output DFA.
- If I can actually figure out a way to print to the canvas, save button should also save a png.
- Probably a built version of the app, so no time wasted compiling.

## NFA File Structure

Examples can be found under tests folder. A good example to explain our structure is **test4**.

Program takes this input...

```plaintext
4
abc
1 3
0
0 a 1
1 b 3
0 @ 2
2 c 2
2 @ 3
```

and returns this output...

```plaintext
4
abc
3 0 2 3
0
0 a 1
0 c 2
1 b 3
2 c 2
```

### Explanation for both Input and Output

First line dictates how many nodes there are. Here, we have 4 of them. Second line dictates the symbols, them being "a", "b" and "c" for our case. Third line dictates final states and fourth dictates the starting state.

So far, our NFA has 4 nodes with the "abc" language, 1st and 3rd nodes are it's final states and 0th state is it's start state.

Next N lines with the "Number Symbol Number" syntax describe the routes. 0 a 1 means you'd reach to the 1st node from 0th if you used the "a" symbol.

We have one special symbol, "@", and it is used for Lambda. Really simplified, Lambda is what you use when you want to reach to a certain state without using a symbol.

## Saving Files

Files are saved at the selected file's location. You don't need to convert first. Selecting a file and hitting the save button will save the output under "filename_output.txt" and it is the same output you see on console.
