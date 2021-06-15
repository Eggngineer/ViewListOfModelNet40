### We visiblize the List of ModelNet40H5Files.

I was struggling to check what model this is in the ModelNet40 dataset files. So I made pyfiles that returns the list which types of the models these are.

* dataloader.py: load data from modelnet h5 files.
* RelatePcdToNames.py: make the list of model from
  ```
  ply_data_train_?_id2file.json
  ```
TD;TR:
```python
git clone https://github.com/Eggngineer/ViewListOfModelNet40
```

