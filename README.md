# Padeiro: The sourdough bread baker's assistant

Render sourdough bread recipes expressed as baker's percentages into actual
ingredient weights given the total flour weight.

## NOTE: Not everything listed below is implemented.

The features listed below were created as guidelines for what the project
should look like. Not everything is currently implemented (or will be 
implemented).

## Usage

### From the command line

To list options, run `padeiro --help`:

```
padeiro RECIPE FLOUR_WEIGHT


```

To render the `basic` recipe from the built-in cookbook:

```
$ padeiro basic 1000
A basic sourdough loaf
----------------------

Levain:
* Flour:
  * Whole wheat: 100 g
* Liquid:
  * Water: 100 g
  
Dough:
* Flour:
  * Whole wheat: 200 g
  * White: 700 g
* Liquid:
  * Water: 530 g
* Extra:
  * Salt: 20 g
 
Instructions:

Mix the levain with a teaspoon of starter and let it sit overnight.
The next morning, mix the levain with the water and then add the rest of the flour.
Mix until the flour and water are incorporated and let sit for 40 minutes.
Add the salt and mix with a folding and pinching process.
Knead for 5-15 minutes.
Bulk fermentation for 3-6 hours depending on the room temperature.
Do sets of stretch-and-fold during bulk fermentation.
Divide the dough, shape, and transfer to proofing containers (could be a bowl 
with a floured tea towel).
Proof overnight in the fridge.
Back the next morning in a pre-heated dutch oven: 30 minutes at 250C with the lid on,
then 25-35 minutes at 210C with the lid off.

Author: Leonardo Uieda
Source: https://github.com/leouieda/padeiro/raw/master/recipes/basic.toml
```

## As a Python library

All functionality from the command line program can be accessed through
the underlying Python library:

```python
import padeiro

recipe = padeiro.fetch("basic")
rendered_recipe = padeiro.render(recipe, flour_weight=1000)
padeiro.display(rendered_recipe)
```

## License

This is free software: you can redistribute it and/or modify it under the terms of the 
MIT License. A copy of this license is provided in 
[LICENSE.txt](https://github.com/leouieda/padeiro/blob/master/LICENSE.txt).
