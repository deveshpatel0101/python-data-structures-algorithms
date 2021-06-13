# Python Data Structures and Algorithms

Data Structures and Algorithms (DSA) is one of the most important topics in computer science that every CS student must be proficient in and even non-CS students must have basic understanding of it. It is said that DSA is like bread and butter, necessity of CS. This repository is made for those students (like me :sunglasses:) who are eager to learn and want to implement data structures and algorithms.

### Instructions

1. To get started make sure that you have python v3+ installed on your computer.
2. Once python is installed on your machine, just clone or download this repository.
3. Now `cd <folder-name>` into downloaded repo.
4. Now run `pytest .` to run all tests or `pytest <folder-name>` to run specific tests.

### Example

Let's assume that you want to run tests for `stack`, then the syntax to run it would be:

```
cd python-data-structures-algorithms
pytest stack
```

### Data Structures

<table>
  <tr>
    <th>Name</th>
    <th>Time Complexity</th>
    <th>Space Complexity</th>
    <th>Description</th>
  </tr>
  <tr>
    <th colspan="4">Graphs</th>
  </tr>
  <tr>
    <td>Directed Unweighted</td>
    <td>-</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Directed Weighted</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Undirected Unweighted</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Undirected Weighted</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <th colspan="4">Heaps</th>
  </tr>
  <tr>
    <td>Max Binary Heap</td>
    <td>insert, delete: O(log(n))</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <td>Min Binary Heap</td>
    <td>insert, delete: O(log(n))</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <th colspan="4">Linked Lists</th>
  </tr>
  <tr>
    <td>Circular Doubly LL</td>
    <td>
      push, pop, shift, unshift: O(1)
      <br />
      insertMiddle, deleteMiddle: O(k)
    </td>
    <td>O(n)</td>
    <td>
      n: # of elements
      <br />
      k: pos of node to act on
    </td>
  </tr>
  <tr>
    <td>Circular LL</td>
    <td>
      push, pop, shift, unshift: O(1)
      <br />
      insertMiddle, deleteMiddle: O(k)
    </td>
    <td>O(n)</td>
    <td>
      n: # of elements
      <br />
      k: pos of node to act on
    </td>
  </tr>
  <tr>
    <td>Doubly LL</td>
    <td>
      push, pop, shift, unshift: O(1)
      <br />
      insertMiddle, deleteMiddle: O(k)
    </td>
    <td>O(n)</td>
    <td>
      n: # of elements
      <br />
      k: pos of node to act on
    </td>
  </tr>
  <tr>
    <td>Singly LL with preserve order</td>
    <td>
      pop, shift: O(1)
      <br />
      insert: O(n)
      <br />
      delete: O(k)
    </td>
    <td>O(n)</td>
    <td>
      n: # of elements
      <br />
      k: pos of node to act on
    </td>
  </tr>
  <tr>
    <td>Singly LL</td>
    <td>
      push, pop, shift, unshift: O(1)
      <br />
      insertMiddle, deleteMiddle: O(k)
    </td>
    <td>O(n)</td>
    <td>
      n: # of elements
      <br />
      k: pos of node to act on
    </td>
  </tr>
  <tr>
    <th colspan="4">Queues</th>
  </tr>
  <tr>
    <td>Circular Double Ended Q</td>
    <td>insert, delete: O(1)</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <td>Circular Q</td>
    <td>insert, delete: O(1)</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <td>Double Ended Q</td>
    <td>insert, delete: O(1)</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <td>Priority Q</td>
    <td>insert, delete: O(log(n))</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <td>Simple Q</td>
    <td>insert, delete: O(1)</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <th colspan="4">Stack</th>
  </tr>
  <tr>
    <td>Stack</td>
    <td>push, pop: O(1)</td>
    <td>O(n)</td>
    <td>n: # of elements</td>
  </tr>
  <tr>
    <th colspan="4">Trees</th>
  </tr>
  <tr>
    <td>AVL Trees</td>
    <td>
      Insert: O(h)
      <br />
      BFS, DFS(In, Pre, or Post): O(n)
    </td>
    <td>
      Insert: O(h)
      <br />
      BFS, DFS(In, Pre or Post): O(n)
    </td>
    <td>
      h: height of the tree
      <br />
      n: # of nodes
    </td>
  </tr>
  <tr>
    <td>Binary Search Tree</td>
    <td>
      Insert: O(n)
      <br />
      BFS, DFS(In, Pre, or Post): O(n)
    </td>
    <td>
      Insert: O(h)
      <br />
      BFS, DFS(In, Pre or Post): O(n)
    </td>
    <td>
      h: height of the tree
      <br />
      n: # of nodes
    </td>
  </tr>
  <tr>
    <td>Simple Binary Tree</td>
    <td>
      Insert: O(n)
      <br />
      BFS, DFS(In, Pre, or Post): O(n)
    </td>
    <td>
      Insert: O(n)
      <br />
      BFS, DFS(In, Pre, or Post): O(n)
    </td>
    <td>
      h: height of the tree
      <br />
      n: # of nodes
    </td>
  </tr>
</table>
<br />

### Algorithms

<table>
  <tr>
    <th>Name</th>
    <th>Time Complexity</th>
    <th>Space Complexity</th>
    <th>Description</th>
  </tr>
  <tr>
      <th colspan="4">Searching</th>
  </tr>
  <tr>
      <td>Binary Search</td>
      <td>O(log(n))</td>
      <td>O(1)</td>
      <td>n: # of elements</td>
  </tr>
  <tr>
      <td>Interpolation Search</td>
      <td>
        Avg Case: O(log<sub>2</sub>(log<sub>2</sub>(n)))
        <br />
        O(n) when items are distributed exponentially
      </td>
      <td>O(1)</td>
      <td>n: # of elements</td>
  </tr>
  <tr>
      <td>Linear Search</td>
      <td>O(n)</td>
      <td>O(1)</td>
      <td>n: # of elements</td>
  </tr>
  <tr>
      <td>Ternary Search</td>
      <td>O(log<sub>3</sub>(n))</td>
      <td>O(1)</td>
      <td>n: # of elements</td>
  </tr>
  <tr>
    <th colspan="4">Sorting</th>
  </tr>
  <tr>
    <td>Binary Insertion Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(n)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Bubble Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Bucket Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Counting Sort</td>
    <td>O(n + k)</td>
    <td>O(k)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Heap Sort</td>
    <td>O(nLog(n))</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Insertion Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Merge Sort</td>
    <td>O(nLog(n))</td>
    <td>O(n)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Quick Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(log(n))</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Radix Sort</td>
    <td>O(nk)</td>
    <td>O(n+k)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Selection Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Shell Sort</td>
    <td>O(n<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>-</td>
  </tr>
</table>

### Contribution

This repository is for learning how to implement data structures and algorithms, and since contributions of others won't really teach me how to implement it by myself, I won't be accepting any pull requests. However, feel free to fork this repo and modify the code to play around various data structures and algorithms. Moreover, while playing around the code, if you find anything unusual or wrong in the implemetation, I would highly appreciate if you create an issue on the same.

### License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT). In short, this means you are free to use this software in any personal, open-source or commercial projects. Attribution is optional but appreciated.

```
HAPPY CODING 💻
HAPPY LEARNING 📚
```
