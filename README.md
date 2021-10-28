# Bengali Geonames Python Library (Python 3)

This project allows you to get the equivalent Bengali classification for a certain geonames feature.
You can enter the feature code and retrieve the Bengali classification.
You can also enter the english feature code and retrieve the Bengali classification.

```python

import src.classification as bg

bg.get_bengali_class_from_feature_code("AAA")
# or
bg.get_bengali_class_from_english_feature("zone")
```