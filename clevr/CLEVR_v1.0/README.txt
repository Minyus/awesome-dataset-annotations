The data is organized into the following directory structure:

images/
  train/
    CLEVR_train_000000.png
    CLEVR_train_000001.png
    [...]
    CLEVR_train_069999.png
  val/
    CLEVR_val_000000.png
    [...]
    CLEVR_val_014999.png
  test/
    CLEVR_test_000000.png
    [...]
    CLEVR_test_014999.png
scenes/
  CLEVR_train_scenes.json
  CLEVR_val_scenes.json
questions/
  CLEVR_train_questions.json
  CLEVR_val_questions.json
  CLEVR_test_questions.json


SCENE FILE FORMAT
Each of the scene files has the following format:

{
  "info": <info>,
  "scenes": [<scene>]
}

<info> {
  "split": <string: "train", "val", or "test">,
  "version": <string>,
  "date": <string>,
  "license": <string>,
}

<scene> {
  "spit": <string: "train", "val", or "test">,
  "image_index": <integer>,
  "image_filename": <string, e.g. "CLEVR_train_000000.png">,
  "directions": {
    "left": [list of 3 numbers x, y, z],
    "right": [list of 3 numbers x, y, z],
    "front": [list of 3 numbers x, y, z],
    "behind": [list of 3 numbers x, y, z],
    "below": [list of 3 numbers x, y, z],
    "above": [list of 3 numbers x, y, z]
  },
  "objects": [<object>],
  "relations": {
    "left": <adjacency list>,
    "right": <adjacency list>,
    "front": <adjacency list>,
    "behind": <adjacency list>
  }
}

Relationships are stored as adjacency lists, which are lists of lists of
integers. If s is a <scene> object, then s['relations']['left'][i] is a list of
indices for objects which are left of s['objects'][i].

In other words, s['objects'][j] is left of s['objects'][i] if and only if
j is in s['relations']['left'][i].

<object> {
  "3d_coords": [list of 3 numbers x, y, z],
  "pixel_coords": [list of 3 numbers x, y, z],
  "rotation": <number, in degrees>,
  "size': <string: "small" or "large">,
  "color": <string: "gray", "blue", "brown", "yellow", "red", "green", "purple", or "cyan">,
  "material": <string: "rubber" or "metal">,
  "shape": <string: "cube", "sphere", or "cylinder">
}


QUESTION FILE FORMAT
Each of the question files has the following format:

{
  "info": <info>,
  "questions": [<question>]
}

<info> {
  "split": <string: "train", "val", or "test">,
  "version": <string>,
  "date": <string>,
  "license": <string>
}

<question> {
  "split": <string: "train", "val", or "test">,
  "image_index": <integer>,
  "image_filename": <string, e.g. "CLEVR_train_000000.png">,
  "question": <string>,
  "answer": <string>,
  "program": [<function>],
  "question_family_index': <integer>,
}

Answers and programs are omitted from the test data.

<function> {
  "function": <string, e.g. "filter_color">,
  "inputs": [list of integer],
  "value_inputs": [list of strings],
}

Programs are represented as lists of functions. Each function may take as input
both literal values (given in "value_inputs") and output from other functions
(given in "inputs"). Functions are guaranteed to be sorted topologically, so
that j in program[i]['inputs'] if and only if j < i.

As a simple example, consider the question "How many blue cubes are there?"

The program representation for this question would be:

[
  {
    "function": "scene",
    "inputs": [],
    "value_inputs": []
  },
  {
    "function": "filter_color",
    "inputs": [0],
    "value_inputs": ["blue"]
  },
  {
    "function": "filter_shape",
    "inputs": [1],
    "value_inputs": ["cube"]
  },
  {
    "function": "count",
    "inputs": [2],
    "value_inputs": []
  }
]

Note that all programs contain one or more "scene" functions; this is a special
function that takes no inputs, and outputs the set of all objects in the scene.

