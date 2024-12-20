# DefFiller
This is the repository for "DefFiller: Mask-Conditioned Diffusion for Salient Steel Surface Defect Generation".

## Dataset
1. Download [SD-saliency-900](https://drive.google.com/file/d/1yQdfow1-WvDilQTZ1zj1EbbErN1DksVF/view?usp=sharing)
2. Place the masks in the directory "./DATA/SD-saliency-900/Ground_truth" and the images in "./DATA/SD-saliency-900/Source_Images".
3. Generate a "caption.json" file for the dataset by referring to "./DATA/process_json.py".

## Env Install
We follow [GLIGEN](https://github.com/gligen/GLIGEN).

## Train
1. Download the pre-trained model [here](https://huggingface.co/gligen/gligen-generation-sem/blob/main/diffusion_pytorch_model.bin).
2. Put it on the directory named "./model_sem", and rename it to "sem_diffusion_pytorch_model.bin".
3. Start to train:
```
   #python main.py --name=your_experiment_name  -- OUTPUT_ROOT=save_path
```
The experiment will be saved in “OUTPUT_ROOT/name”.

## Inference
```
   #python infer.py
```
Example samples for each checkpoint will be saved in “generation_samples”.


