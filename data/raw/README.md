# A Benchmark Dataset for Code-Level Vulnerability Detection and Analysis
# PyCode-Vul

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
![Task](https://img.shields.io/badge/task-vulnerability--detection-orange)
![Language](https://img.shields.io/badge/language-Python-brightgreen)
[![Zenodo](https://img.shields.io/badge/Zenodo-19746552-blue)](https://zenodo.org/records/19746552)


PyCode-Vul is a real-world Python vulnerability dataset accepted at IEEE BigData 2025. The dataset was created by mining security-related commits from widely used Python GitHub repositories, extracting changed files, identifying changed lines, recovering before/after code, validating Python functions through AST parsing, applying CWE mapping, and removing duplicate samples.

The dataset is designed for code-level vulnerability detection, vulnerability classification, and empirical evaluation of code pre-trained models.

---


## Dataset Construction Pipeline

The following figure summarizes the PyCode-Vul dataset construction process, including repository mining, commit filtering, diff/hunk extraction, before/after code extraction, Python code filtering, AST validation, CWE mapping, Bandit-based heuristic analysis, duplication checking, and final dataset creation.

## Dataset Construction Pipeline

![PyCode-Vul Dataset Construction Pipeline](https://drive.google.com/uc?export=view&id=1k6ynczAftDqCBUV9GNla59LMCk3Lo3Uu)

---

## Dataset Sources

PyCode-Vul was collected from 15 real-world Python repositories covering web frameworks, security tools, DevOps automation, machine learning lifecycle management, data workflow systems, networking libraries, and digital forensics tools.

| Repository | Samples | Purpose | Real-World Use |
|---|---:|---|---|
| Sqlmap | 1000 | SQL injection testing tool | Widely used in penetration testing and security research |
| Django | 835 | Web framework | Used for scalable production web applications |
| Salt | 1006 | Automation and configuration management | Commonly used in DevOps and infrastructure automation |
| Airflow | 731 | Workflow orchestration | Used for data pipeline scheduling and management |
| Ansible | 727 | IT automation framework | Enables large-scale configuration and deployment management |
| Mlflow | 812 | ML lifecycle management | Used for experiment tracking and model deployment |
| W3af | 776 | Web application security scanner | Detects security vulnerabilities in web applications |
| Tornado | 423 | Web server and networking framework | Used in asynchronous and real-time web services |
| Jupyter | 369 | Interactive computing environment | Core platform for data science and AI research |
| Bandit | 310 | Security static analyzer | Identifies insecure coding practices in Python |
| Volatility | 241 | Memory forensics framework | Used in digital forensics and incident response |
| Flask | 141 | Lightweight web framework | Used for API and microservice development |
| Paramiko | 336 | SSH communication library | Used for secure remote automation and data transfer |
| Requests | 139 | HTTP networking library | Standard Python library for web communication |
| Yaml | 53 | YAML parsing and serialization | Used for configuration management and data exchange |
| **Total** | **7899** |  |  |

---

## Dataset Files

The dataset is provided with train and test splits.

| File | Description |
|---|---|
| `train.csv` | Training split of the PyCode-Vul dataset |
| `test.csv` | Test split of the PyCode-Vul dataset |

Each sample may contain Python code, repository information, commit information, before/after function information, changed lines, hashes, and vulnerability-related labels or metadata.

---

## Experimental Results

The paper evaluates several CodePTMs on PyCode-Vul and benchmark vulnerability datasets, including CVEFixes, VUDENC, Code_Vulnerability_Python, Buggy_Python, Py Data, PCV+Merge, and PyCode-Vul Test.

The models include CodeBERT, CodeGPT, CodeBERTa, DeBERTa-v3, CodeParrot, GraphCodeBERT, DistilBERT, UniXcoder, CodeGen-Mono, and CodeT5+.

The following table reports the full performance assessment from the paper.


### Table IV. Performance Assessment of Fine-Tuned CodePTMs on the PyCode_Vul Dataset

**Notes**
- **Δ** represents the aggregated test datasets: CVEFixes, VUDENC, Code_Vulnerability_Python, Buggy_Python, Py Data, and PyCode_Vul Test.
- **★** denotes results evaluated on the PyCode_Vul testing set.
- **\*** indicates the best performance.
- Values without the asterisk represent the second-best result.

---

### CVEFixes

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.5391 | 0.6626 | 0.1594 | 0.9188 | 0.2570 | 0.1202 | 0.0782 | 0.4608 | 0.4608 | 0.6393 |
| CodeGPT | 0.5391 | 0.8648 | 0.0927 | 0.9855 | 0.1675 | 0.1737 | 0.0782 | 0.4608 | 0.4608 | 0.6663 |
| CodeBERTa | 0.5304 | 0.7333 | 0.0950 | 0.9652 | 0.1692 | 0.1232 | 0.0608 | 0.4695 | 0.4695 | 0.6335 |
| DeBERTa-v3 | 0.5492 | 0.7931 | 0.1333 | 0.9652 | 0.2282 | 0.1775 | 0.0985 | 0.4507 | 0.4507 | 0.6780 |
| CodeParrot | 0.5565 | 0.7600 | 0.1652 | 0.9478 | 0.2714 | 0.1815 | 0.1130 | 0.4434 | 0.4434 | 0.6581 |
| GraphCodeBERT | 0.5333 | 0.6533 | 0.1420 | 0.9246 | 0.2333 | 0.1070 | 0.0666 | 0.4666 | 0.4666 | 0.6559 |
| DistilBERT | 0.5478 | 0.6736 | 0.1855 | 0.9101 | 0.2909 | 0.1388 | 0.0956 | 0.4521 | 0.4521 | 0.6113 |
| UniXcoder | 0.5362 | 0.6506 | 0.1565 | 0.9159 | 0.2523 | 0.1113 | 0.0724 | 0.4637 | 0.4637 | 0.6222 |
| CodeGen-Mono | 0.5347 | 0.7000 | 0.1217 | 0.9478 | 0.2074 | 0.1234 | 0.0695 | 0.4652 | 0.4652 | 0.6350 |
| CodeT5+ | 0.5318 | 0.6617 | 0.1304 | 0.9333 | 0.2179 | 0.1069 | 0.0637 | 0.4681 | 0.4681 | 0.6329 |

---

### VUDENC

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.5811 | 0.7433 | 0.2477 | 0.9144 | 0.3711 | 0.2176 | 0.1622 | 0.4188 | 0.4188 | 0.7085 |
| CodeGPT | 0.5793 | 0.8617 | 0.1889 | 0.9609 | 0.3099 | 0.2538 | 0.1586 | 0.4206 | 0.4206 | 0.6714 |
| CodeBERTa | 0.6247 | 0.8333 | 0.3119 | 0.9376 | 0.4530 | 0.3199 | 0.2495 | 0.3752 | 0.3752 | 0.7700 |
| DeBERTa-v3 | 0.5962 | 0.8139 | 0.2495 | 0.9429 | 0.3819 | 0.2671 | 0.1925 | 0.4037 | 0.4037 | 0.7530 |
| CodeParrot | 0.6310 | 0.8295 | 0.3207 | 0.9322 | 0.4719 | 0.3283 | 0.2620 | 0.3689 | 0.3689 | 0.7299 |
| GraphCodeBERT | 0.6096 | 0.8090 | 0.2869 | 0.9322 | 0.4236 | 0.2869 | 0.2192 | 0.3903 | 0.3903 | 0.7184 |
| DistilBERT | 0.5333 | 0.5714 | 0.2666 | 0.8000 | 0.3636 | 0.0788 | 0.0666 | 0.4666 | 0.4666 | 0.5866 |
| UniXcoder | 0.5784 | 0.7933 | 0.2121 | 0.9447 | 0.3347 | 0.2304 | 0.1568 | 0.4215 | 0.4215 | 0.6894 |
| CodeGen-Mono | 0.5333 | 0.6000 | 0.2000 | 0.8666 | 0.3000 | 0.0894 | 0.0666 | 0.4666 | 0.4666 | 0.4577 |
| CodeT5+ | 0.5819 | 0.7911 | 0.2228 | 0.9411 | 0.3477 | 0.2357 | 0.1639 | 0.4180 | 0.4180 | 0.6721 |

---

### Code_vulnerability_python

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.4787 | 0.4838 | 0.6367 | 0.3207 | 0.5498 | -0.0447 | -0.0424 | 0.5212 | 0.5212 | 0.5337 |
| CodeGPT | 0.5247 | 0.5221 | 0.5825 | 0.4669 | 0.5507 | 0.0498 | 0.0495 | 0.4752 | 0.4752 | 0.4575 |
| CodeBERTa | 0.5259 | 0.5205 | 0.6556 | 0.3962 | 0.5803 | 0.0518 | 0.0518 | 0.4740 | 0.4740 | 0.5387 |
| DeBERTa-v3 | 0.5283 | 0.5235 | 0.6297 | 0.4268 | 0.5717 | 0.0578 | 0.0566 | 0.4716 | 0.4716 | 0.5295 |
| CodeParrot | 0.5141 | 0.5090 | 0.7971 | 0.2311 | 0.6213 | 0.0343 | 0.0283 | 0.4858 | 0.4858 | 0.5011 |
| GraphCodeBERT | 0.5129 | 0.5088 | 0.7476 | 0.2783 | 0.6055 | 0.0293 | 0.0259 | 0.4870 | 0.4870 | 0.5726 |
| DistilBERT | 0.5341 | 0.5324 | 0.5613 | 0.5070 | 0.5464 | 0.0684 | 0.0683 | 0.4658 | 0.4658 | 0.5230 |
| UniXcoder | 0.5424 | 0.5302 | 0.7452 | 0.3396 | 0.6196 | 0.0928 | 0.0400 | 0.4575 | 0.4575 | 0.5872 |
| CodeGen-Mono | 0.4492 | 0.4188 | 0.2617 | 0.6367 | 0.3222 | -0.1093 | -0.1014 | 0.5507 | 0.5507 | 0.4394 |
| CodeT5+ | 0.5165 | 0.5128 | 0.6603 | 0.3726 | 0.5773 | 0.0344 | 0.0330 | 0.4834 | 0.4834 | 0.5561 |

---

### Train Dataset: PyCode_Vul | Test Dataset: Buggy_python

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.5173 | 0.6394 | 0.0769 | 0.9550 | 0.1417 | 0.0718 | 0.0347 | 0.4826 | 0.4826 | 0.4819 |
| CodeGPT | 0.5179 | 0.6376 | 0.0832 | 0.9526 | 0.1473 | 0.0727 | 0.0359 | 0.4820 | 0.4820 | 0.4865 |
| CodeBERTa | 0.5176 | 0.6439 | 0.0790 | 0.9562 | 0.1408 | 0.0736 | 0.0353 | 0.4823 | 0.4823 | 0.5243 |
| DeBERTa-v3 | 0.5173 | 0.6435 | 0.0778 | 0.9568 | 0.1389 | 0.0728 | 0.0347 | 0.4826 | 0.4826 | 0.4907 |
| CodeParrot | 0.5158 | 0.6280 | 0.0778 | 0.9538 | 0.1385 | 0.0658 | 0.0317 | 0.4841 | 0.4841 | 0.5629 |
| GraphCodeBERT | 0.5161 | 0.5363 | 0.0754 | 0.9568 | 0.1349 | 0.0684 | 0.0323 | 0.4838 | 0.4838 | 0.4336 |
| DistilBERT | 0.5173 | 0.6394 | 0.0763 | 0.9550 | 0.1417 | 0.0718 | 0.0347 | 0.4826 | 0.4826 | 0.5121 |
| UniXcoder | 0.5158 | 0.6345 | 0.0748 | 0.9568 | 0.1330 | 0.0673 | 0.0317 | 0.4841 | 0.4841 | 0.4242 |
| CodeGen-Mono | 0.5131 | 0.5814 | 0.0940 | 0.9322 | 0.1619 | 0.0483 | 0.0263 | 0.4868 | 0.4868 | 0.6046 |
| CodeT5+ | 0.5173 | 0.6380 | 0.0802 | 0.9544 | 0.1426 | 0.0711 | 0.0347 | 0.4826 | 0.4826 | 0.5347 |

---

### Train Dataset: PyCode_Vul | Test Dataset: Py Data

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.5666 | 0.6666 | 0.2666 | 0.8666 | 0.3809 | 0.1666 | 0.1333 | 0.4333 | 0.4333 | 0.5955 |
| CodeGPT | 0.5333 | 0.5714 | 0.2666 | 0.8000 | 0.3636 | 0.0788 | 0.0666 | 0.4666 | 0.4666 | 0.5444 |
| CodeBERTa | 0.5666 | 0.6666 | 0.2666 | 0.8666 | 0.3809 | 0.1666 | 0.1333 | 0.4333 | 0.4333 | 0.6266 |
| DeBERTa-v3 | 0.5666 | 0.6666 | 0.2666 | 0.8666 | 0.3809 | 0.1666 | 0.1333 | 0.4333 | 0.4333 | 0.6000 |
| CodeParrot | 0.5666 | 0.6000 | 0.4000 | 0.7333 | 0.4800 | 0.1414 | 0.1313 | 0.4333 | 0.4333 | 0.4977 |
| GraphCodeBERT | 0.5666 | 0.6666 | 0.2666 | 0.8666 | 0.3809 | 0.1666 | 0.1333 | 0.4333 | 0.4333 | 0.5111 |
| DistilBERT | 0.5333 | 0.5714 | 0.2666 | 0.8000 | 0.3636 | 0.0788 | 0.0666 | 0.4666 | 0.4666 | 0.5866 |
| UniXcoder | 0.6000 | 0.7142 | 0.3333 | 0.8666 | 0.4450 | 0.2364 | 0.1999 | 0.4000 | 0.4000 | 0.6133 |
| CodeGen-Mono | 0.5333 | 0.6000 | 0.2000 | 0.8666 | 0.3000 | 0.0894 | 0.0666 | 0.4666 | 0.4666 | 0.4577 |
| CodeT5+ | 0.5666 | 0.6666 | 0.2666 | 0.8666 | 0.3809 | 0.1666 | 0.1333 | 0.4333 | 0.4333 | 0.5688 |

---

### PCV+MergeΔ

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.7858 | 0.9461 | 0.6244 | 0.9613 | 0.7523 | 0.6161 | 0.5772 | 0.2141 | 0.2141 | 0.7872 |
| CodeGPT | 0.7870 | 0.9650 | 0.6133 | 0.9758 | 0.7500 | 0.6254 | 0.5799 | 0.2129 | 0.2129 | 0.8801 |
| CodeBERTa | 0.7962 | 0.9670 | 0.6303 | 0.9766 | 0.7632 | 0.6403 | 0.5979 | 0.2037 | 0.2037 | 0.8372 |
| DeBERTa-v3 | 0.7901 | 0.9613 | 0.6222 | 0.9726 | 0.7553 | 0.6285 | 0.5858 | 0.2098 | 0.2098 | 0.7835 |
| CodeParrot | 0.7959 | 0.9525 | 0.6400 | 0.9653 | 0.7656 | 0.6340 | 0.5968 | 0.2040 | 0.2040 | 0.8671 |
| GraphCodeBERT | 0.7951 | 0.9140 | 0.6392 | 0.9645 | 0.7647 | 0.6324 | 0.5953 | 0.2048 | 0.2048 | 0.8038 |
| DistilBERT | 0.7974 | 0.9598 | 0.6377 | 0.9710 | 0.7663 | 0.6393 | 0.6000 | 0.2025 | 0.2025 | 0.8512 |
| UniXcoder | 0.7935 | 0.9594 | 0.6303 | 0.9710 | 0.7608 | 0.6332 | 0.5925 | 0.2064 | 0.2034 | 0.7711 |
| CodeGen-Mono | 0.7677 | 0.9348 | 0.5955 | 0.9549 | 0.7276 | 0.5840 | 0.5416 | 0.2322 | 0.2322 | 0.8019 |
| CodeT5+ | 0.7889 | 0.9588 | 0.6214 | 0.9710 | 0.7541 | 0.6259 | 0.5835 | 0.2110 | 0.2110 | 0.8329 |

---

### PyCode_Vul Test★

| Model | Acc. | Pre. | Rec. | Spe. | F1. | MCC | Kappa. | MSE | MAE | AUC. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeBERT | 0.9614 | 0.9572 | 0.9556 | 0.9659 | 0.9564 | 0.9217 | 0.9217 | 0.0385 | 0.0385 | 0.9608 |
| CodeGPT | 0.9621 | 0.9501 | 0.9651 | 0.9596 | 0.9576 | 0.9234 | 0.9233 | 0.0378 | 0.0378 | 0.9836 |
| CodeBERTa | 0.9775 | 0.9716 | 0.9778 | 0.9773 | 0.9747 | 0.9545 | 0.9545 | 0.0224 | 0.0224 | 0.9954* |
| DeBERTa-v3 | 0.9761 | 0.9776 | 0.9683 | 0.9823* | 0.9729 | 0.9516 | 0.9516 | 0.0238 | 0.0238 | 0.9941 |
| CodeParrot | 0.9515 | 0.9350 | 0.9572 | 0.9470 | 0.9460 | 0.9023 | 0.8984 | 0.0484 | 0.0484 | 0.9804 |
| GraphCodeBERT | 0.9621 | 0.9529 | 0.9620 | 0.9621 | 0.9574 | 0.9233 | 0.9233 | 0.0370 | 0.0370 | 0.9621 |
| DistilBERT | 0.9677 | 0.9665 | 0.9604 | 0.9735 | 0.9634 | 0.9345 | 0.9345 | 0.0322 | 0.0322 | 0.9669 |
| UniXcoder | 0.9810* | 0.9778* | 0.9794* | 0.9823* | 0.9786* | 0.9616* | 0.9616 | 0.0189* | 0.0189* | 0.9808 |
| CodeGen-Mono | 0.9038 | 0.9024 | 0.8781 | 0.9243 | 0.8901 | 0.8022 | 0.8046 | 0.0961 | 0.0961 | 0.9012 |
| CodeT5+ | 0.9754 | 0.9686 | 0.9762 | 0.9747 | 0.9724 | 0.9503 | 0.9502 | 0.0245 | 0.0245 | 0.9755 |




### Key Result Summary

On the PyCode-Vul Test set, the evaluated models achieved strong performance. UniXcoder obtained the best reported performance across several metrics, including accuracy, precision, recall, specificity, F1, MCC, Kappa, MSE, and MAE. CodeBERTa achieved the highest AUC score in the reported table.

---
## Related Links

- Hugging Face: https://huggingface.co/datasets/S-AIR-L/PyCode-Vul
- Zenodo DOI/Archive: https://zenodo.org/records/19746552
- GitHub: https://github.com/S-AiRLab/-PyCode_Vul-A-Benchmark-Dataset-for-Code-Level-Vulnerability-Detection-and-Analysis/tree/main
- Kaggle: https://www.kaggle.com/datasets/oulabspring/pycode-vul-a-benchmark-dataset-for-python/data

## Citation

If you use **PyCode-Vul** in your research, please cite the following paper:

**A Benchmark Dataset for Code-Level Vulnerability Detection and Analysis**  
Tasmin Karim, Mst Shapna Akter, and Alfredo Cuzzocrea.  
In *2025 IEEE International Conference on Big Data (BigData)*, pp. 4237–4246, IEEE, 2025.

```bibtex
@inproceedings{karim2025benchmark,
  title={A Benchmark Dataset for Code-Level Vulnerability Detection and Analysis},
  author={Karim, Tasmin and Akter, Mst Shapna and Cuzzocrea, Alfredo},
  booktitle={2025 IEEE International Conference on Big Data (BigData)},
  pages={4237--4246},
  year={2025},
  organization={IEEE}
}


