# DefFiller
This is the repository for "DefFiller: Mask-Conditioned Diffusion for Salient Steel Surface Defect Generation".

## Dataset
Download [SD-saliency-900](https://drive.google.com/file/d/1yQdfow1-WvDilQTZ1zj1EbbErN1DksVF/view?usp=sharing)
And put it on the directory named "./DATA"

## Env Install
We follow [GLIGEN](https://github.com/gligen/GLIGEN).

## Train
1. Download the pre-trained model [here](https://huggingface.co/gligen/gligen-generation-sem/blob/main/diffusion_pytorch_model.bin).
2. Put it on the directory named "./model_sem", and rename it to "sem_diffusion_pytorch_model.bin".
3. Start to train:
```
   #python main.py --name=your_experiment_name  -- OUTPUT_ROOT=save_path
```
