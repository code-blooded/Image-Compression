<h1>Image-Compression</h1>
<p>
Compression using various algorithms and Comparision between them :)
</p>
<hr/>
<p>
  To run the median cut algorithm, enter "<b>python main.py</b>" <br>
  <br>
  <b>NOTE</b>: Make changes only to main.py <br>
  <ul>
<li> Depth can be changed by varying the variable depth <br>
<li> Default depth at 5 <br>
<li> Change the path variable to your desired image path <br>
<li> Input files (.csv) contain different channels of blue, green and red for the input image <br>
<li> Output files (.csv) contain noise/error values in each color(r,g,b) for the output image <br>
<li> Lookup table is [start,(end-1)] range to be replaced with value <br>
  </ul>
  <hr/>
 <p> <b> Sample compression using Median Cut Algorithm </b> </p>
<table>
<tr>
  <td><img src="code_blooded.bmp" alt="uncompressed img"/><p> <i>Uncompressed Image</i></p></td>
<td><img src="code_blooded16.bmp" alt="compressed img"/><p> <i>Compressed Image(depth=4)</i></p></td>
</tr>
<tr>
  <td><img src="code_blooded.bmp" alt="uncompressed img"/><p> <i>Uncompressed Image</i></p></td>
<td><img src="code_blooded32.bmp" alt="compressed img"/><p> <i>Compressed Image(depth=5)</i></p></td>
</tr>
</table>
  
  <h6> Note: The compression cannot be seen directly as they are ultimately saved as bmp, but can be seen in the lookup table as only few colours are used. </h6>
</p>
