# Awesome Dataset Annotations

Sample dataset annotations for Vision and Language tasks

## Overview

To check the contents of big annotation JSON files easily, small subsets were extracted and saved as JSON and YAML files using [SmallDict](https://github.com/Minyus/smalldict) Python package.

For each of the JSON annotation file, first 10 items for each list (images, objects, etc) were extracted and saved with suffix:
- `_samples.json` for JSON
- `_samples.yaml` for YAML

## Disclaimer 

The copy rights are preserved by the original owners.
Please refer to the original owners' websites or papers regarding the license.

## Datasets

- clevr

  https://cs.stanford.edu/people/jcjohns/clevr/

- coco

  https://cocodataset.org/#download

- coco2017

  https://cocodataset.org/#download

- textcaps

  https://textvqa.org/textcaps/dataset

- textvqa

  https://textvqa.org/dataset

- vqa2

  https://visualqa.org/download.html

## Dataset Annotation Samples

- clevr
  - [CLEVR_test_questions.json_samples.json](clevr/CLEVR_v1.0/questions/CLEVR_test_questions.json_samples.json)
  - [CLEVR_test_questions.json_samples.yaml](clevr/CLEVR_v1.0/questions/CLEVR_test_questions.json_samples.yaml)
  - [CLEVR_val_questions.json_samples.json](clevr/CLEVR_v1.0/questions/CLEVR_val_questions.json_samples.json)
  - [CLEVR_val_questions.json_samples.yaml](clevr/CLEVR_v1.0/questions/CLEVR_val_questions.json_samples.yaml)
  - [CLEVR_train_scenes.json_samples.json](clevr/CLEVR_v1.0/scenes/CLEVR_train_scenes.json_samples.json)
  - [CLEVR_train_scenes.json_samples.yaml](clevr/CLEVR_v1.0/scenes/CLEVR_train_scenes.json_samples.yaml)
  - [CLEVR_val_scenes.json_samples.json](clevr/CLEVR_v1.0/scenes/CLEVR_val_scenes.json_samples.json)
  - [CLEVR_val_scenes.json_samples.yaml](clevr/CLEVR_v1.0/scenes/CLEVR_val_scenes.json_samples.yaml)
- coco
  - [captions_train2014.json_samples.json](coco/annotations_trainval2014/annotations/captions_train2014.json_samples.json)
  - [captions_train2014.json_samples.yaml](coco/annotations_trainval2014/annotations/captions_train2014.json_samples.yaml)
  - [captions_val2014.json_samples.json](coco/annotations_trainval2014/annotations/captions_val2014.json_samples.json)
  - [captions_val2014.json_samples.yaml](coco/annotations_trainval2014/annotations/captions_val2014.json_samples.yaml)
  - [instances_train2014.json_samples.json](coco/annotations_trainval2014/annotations/instances_train2014.json_samples.json)
  - [instances_train2014.json_samples.yaml](coco/annotations_trainval2014/annotations/instances_train2014.json_samples.yaml)
  - [instances_val2014.json_samples.json](coco/annotations_trainval2014/annotations/instances_val2014.json_samples.json)
  - [instances_val2014.json_samples.yaml](coco/annotations_trainval2014/annotations/instances_val2014.json_samples.yaml)
  - [person_keypoints_train2014.json_samples.json](coco/annotations_trainval2014/annotations/person_keypoints_train2014.json_samples.json)
  - [person_keypoints_train2014.json_samples.yaml](coco/annotations_trainval2014/annotations/person_keypoints_train2014.json_samples.yaml)
  - [person_keypoints_val2014.json_samples.json](coco/annotations_trainval2014/annotations/person_keypoints_val2014.json_samples.json)
  - [person_keypoints_val2014.json_samples.yaml](coco/annotations_trainval2014/annotations/person_keypoints_val2014.json_samples.yaml)
- coco2017
  - [captions_train2017.json_samples.json](coco2017/annotations_trainval2017/annotations/captions_train2017.json_samples.json)
  - [captions_train2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/captions_train2017.json_samples.yaml)
  - [captions_val2017.json_samples.json](coco2017/annotations_trainval2017/annotations/captions_val2017.json_samples.json)
  - [captions_val2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/captions_val2017.json_samples.yaml)
  - [instances_train2017.json_samples.json](coco2017/annotations_trainval2017/annotations/instances_train2017.json_samples.json)
  - [instances_train2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/instances_train2017.json_samples.yaml)
  - [instances_val2017.json_samples.json](coco2017/annotations_trainval2017/annotations/instances_val2017.json_samples.json)
  - [instances_val2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/instances_val2017.json_samples.yaml)
  - [person_keypoints_train2017.json_samples.json](coco2017/annotations_trainval2017/annotations/person_keypoints_train2017.json_samples.json)
  - [person_keypoints_train2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/person_keypoints_train2017.json_samples.yaml)
  - [person_keypoints_val2017.json_samples.json](coco2017/annotations_trainval2017/annotations/person_keypoints_val2017.json_samples.json)
  - [person_keypoints_val2017.json_samples.yaml](coco2017/annotations_trainval2017/annotations/person_keypoints_val2017.json_samples.yaml)
  - [panoptic_train2017.json_samples.json](coco2017/panoptic_annotations_trainval2017/annotations/panoptic_train2017.json_samples.json)
  - [panoptic_train2017.json_samples.yaml](coco2017/panoptic_annotations_trainval2017/annotations/panoptic_train2017.json_samples.yaml)
  - [panoptic_val2017.json_samples.json](coco2017/panoptic_annotations_trainval2017/annotations/panoptic_val2017.json_samples.json)
  - [panoptic_val2017.json_samples.yaml](coco2017/panoptic_annotations_trainval2017/annotations/panoptic_val2017.json_samples.yaml)
  - [stuff_train2017.json_samples.json](coco2017/stuff_annotations_trainval2017/annotations/stuff_train2017.json_samples.json)
  - [stuff_train2017.json_samples.yaml](coco2017/stuff_annotations_trainval2017/annotations/stuff_train2017.json_samples.yaml)
  - [stuff_val2017.json_samples.json](coco2017/stuff_annotations_trainval2017/annotations/stuff_val2017.json_samples.json)
  - [stuff_val2017.json_samples.yaml](coco2017/stuff_annotations_trainval2017/annotations/stuff_val2017.json_samples.yaml)
- textcaps
  - [TextCaps_0.1_train.json_samples.json](textcaps/TextCaps_0.1_train.json_samples.json)
  - [TextCaps_0.1_train.json_samples.yaml](textcaps/TextCaps_0.1_train.json_samples.yaml)
  - [TextCaps_0.1_val.json_samples.json](textcaps/TextCaps_0.1_val.json_samples.json)
  - [TextCaps_0.1_val.json_samples.yaml](textcaps/TextCaps_0.1_val.json_samples.yaml)
- textvqa
  - [TextVQA_0.5.1_train.json_samples.json](textvqa/TextVQA_0.5.1_train.json_samples.json)
  - [TextVQA_0.5.1_train.json_samples.yaml](textvqa/TextVQA_0.5.1_train.json_samples.yaml)
  - [TextVQA_0.5.1_val.json_samples.json](textvqa/TextVQA_0.5.1_val.json_samples.json)
  - [TextVQA_0.5.1_val.json_samples.yaml](textvqa/TextVQA_0.5.1_val.json_samples.yaml)
- vqa2
  - [abstract_v002_train2017_annotations.json_samples.json](vqa2/Annotations_Binary_Train2017_abstract_v002/abstract_v002_train2017_annotations.json_samples.json)
  - [abstract_v002_train2017_annotations.json_samples.yaml](vqa2/Annotations_Binary_Train2017_abstract_v002/abstract_v002_train2017_annotations.json_samples.yaml)
  - [abstract_v002_val2017_annotations.json_samples.json](vqa2/Annotations_Binary_Val2017_abstract_v002/abstract_v002_val2017_annotations.json_samples.json)
  - [abstract_v002_val2017_annotations.json_samples.yaml](vqa2/Annotations_Binary_Val2017_abstract_v002/abstract_v002_val2017_annotations.json_samples.yaml)
  - [abstract_v002_train2015_annotations.json_samples.json](vqa2/Annotations_Train_abstract_v002/abstract_v002_train2015_annotations.json_samples.json)
  - [abstract_v002_train2015_annotations.json_samples.yaml](vqa2/Annotations_Train_abstract_v002/abstract_v002_train2015_annotations.json_samples.yaml)
  - [abstract_v002_val2015_annotations.json_samples.json](vqa2/Annotations_Val_abstract_v002/abstract_v002_val2015_annotations.json_samples.json)
  - [abstract_v002_val2015_annotations.json_samples.yaml](vqa2/Annotations_Val_abstract_v002/abstract_v002_val2015_annotations.json_samples.yaml)
  - [v2_mscoco_train2014_annotations.json_samples.json](vqa2/v2_Annotations_Train_mscoco/v2_mscoco_train2014_annotations.json_samples.json)
  - [v2_mscoco_train2014_annotations.json_samples.yaml](vqa2/v2_Annotations_Train_mscoco/v2_mscoco_train2014_annotations.json_samples.yaml)
  - [v2_mscoco_val2014_annotations.json_samples.json](vqa2/v2_Annotations_Val_mscoco/v2_mscoco_val2014_annotations.json_samples.json)
  - [v2_mscoco_val2014_annotations.json_samples.yaml](vqa2/v2_Annotations_Val_mscoco/v2_mscoco_val2014_annotations.json_samples.yaml)
