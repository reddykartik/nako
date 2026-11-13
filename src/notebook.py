## 
import os
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib tk
##

## {{{ loading dataset
dirname = os.path.join(os.path.abspath(".."), "data", "raw")
train = pd.read_excel(os.path.join(dirname, "train.xlsx"))
test = pd.read_csv(os.path.join(dirname, "test.csv"))
## }}}

## {{{ missing values, dtypes, shapes and nunique
print("TRAIN DATASET:")
print(train.info())
print("\nTEST DATASET:")
print(test.info())
# TRAIN DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 14248 entries, 0 to 14247
# Data columns (total 10 columns):
#  #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   __source_file               7950 non-null   str
#  1   cve_ids                     14248 non-null  str
#  2   cwe_ids                     14248 non-null  str
#  3   file_path                   14248 non-null  str
#  4   label                       14248 non-null  int64
#  5   patched_function_source     14147 non-null  str
#  6   predicted_cwe_ids           8830 non-null   str
#  7   repo                        14248 non-null  str
#  8   sha                         14248 non-null  str
#  9   vulnerable_function_source  14193 non-null  str
# dtypes: int64(1), str(9)
# memory usage: 1.1 MB
# None
# 
# TEST DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 3563 entries, 0 to 3562
# Data columns (total 10 columns):
#  #   Column                   Non-Null Count  Dtype
# ---  ------                   --------------  -----
#  0   __source_file            1962 non-null   str
#  1   cve_ids                  3563 non-null   str
#  2   cwe_ids                  3563 non-null   str
#  3   file_path                3563 non-null   str
#  4   class                    3563 non-null   int64
#  5   patched_function_source  3545 non-null   str
#  6   predicted_cwe_ids        2204 non-null   str
#  7   repo                     3563 non-null   str
#  8   sha                      3563 non-null   str
#  9   function_code            3563 non-null   str
# dtypes: int64(1), str(9)
# memory usage: 278.5 KB
# None
## }}}

## {{{ viewing dataset samples
print("\nTRAINING SAMPLES:")
print(train.sample(10))
# TRAINING SAMPLES:
#                                __source_file  cve_ids  ...                                       sha                         vulnerable_function_source
# 12214                                    NaN  UNKNOWN  ...  9f87313d1aec2f74d006533648907397448dcdc5  def test_skip_none_tasks(self):\n        sessi...
# 4973         functions_for_w3af_with_cwe.csv  UNKNOWN  ...  a10af2dc8666fc9dda9c2d11f11a853acbabf2a1  def quit(self, widget, event):\n        '''Win...
# 9265                                     NaN  UNKNOWN  ...  0f1f9fa3f80b1e57490380704416bd63455e998c  def POST(self, **kwargs):\n        """\n      ...
# 5950        functions_for_flask_with_cwe.csv  UNKNOWN  ...  a40489e0ce89acef2a49b70a571143ef479ca235  def send_file(filename_or_fp, mimetype=None, a...
# 11355                                    NaN  UNKNOWN  ...  b434928e01faf02e222a291f6da6f38233c72e63  def render_tmpl(tmplsrc,\n                    ...
# 3310      functions_for_ansible_with_cwe.csv  UNKNOWN  ...  56937e8972c34842957dec5f6aa8a30256ec27dd  def _set_variables(self, hostvars):\n\n       ...
# 6692   functions_for_volatility_with_cwe.csv  UNKNOWN  ...  8284cbdf5e92437a701e0e5177b66b29ab5f0620  def modification(self, profile):\n        m = ...
# 4210       functions_for_sqlmap_with_cwe.csv  UNKNOWN  ...  578bcb9140c50baa990066ac4e7f67c482f1c2ef  def unionTest():\n    """\n    This method tes...
# 1066      functions_for_airflow_with_cwe.csv  UNKNOWN  ...  bd38225727abb6a0df3f4ea0e6fc68fa388f0632  def structure_data(\n    session: SessionDep,\...
# 578      functions_for_paramiko_with_cwe.csv  UNKNOWN  ...  9e76f38045ef1e24eb2f6ff93d0b68470b237bad  def _async_request(self, fileobj, t, *arg):\n ...
# 
# [10 rows x 10 columns]

print("\nTESTING SAMPLES:")
print(test.sample(10))
# TESTING SAMPLES:
#                            __source_file  cve_ids  ...                                       sha                                      function_code
# 3288   functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  242a555f35aecc2e5f9a5ee9f929577da2820db0  def get_artifact_repo_from_storage_info(\n    ...
# 119                                  NaN  UNKNOWN  ...  b56cb5cc97de074bb0e520f66b79e7eb2d913fb1  def process_file(self, filepath, only_if_updat...
# 936   functions_for_ansible_with_cwe.csv  UNKNOWN  ...  3f22f79e73af4398d03b0c1676bb8efde32ea607  def get_config_value_and_origin(self, config, ...
# 112   functions_for_airflow_with_cwe.csv  UNKNOWN  ...  cb295c351a016c0a10cab07f2a628b865cff3ca3  def _redact_all(self, item: Redactable, depth:...
# 1832     functions_for_salt_with_cwe.csv  UNKNOWN  ...  fe277909396bf072048e42a27a8d83e1df3547ae  def tune_in(self):\n        '''\n        Lock ...
# 3458                                 NaN  UNKNOWN  ...  adcdf30b2aaf9f5767acc5efe31db1d77417bf5f  def test_is_in_databricks_runtime():\n    with...
# 2505   functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  d46dd96d60002ef0105f3eae8f76a829945dfc3f  def test_get_store_raises_on_uc_uri(store_uri)...
# 2343   functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  9ebab719e53fb3924ea21434d4fe45b9868daf8a  def load_context(self, context):\n            ...
# 3166                                 NaN  UNKNOWN  ...  8f96fa61a7abb8129a7dcfabf216f4ba0b362db5  def admin_password_present(name, password=None...
# 2561   functions_for_django_with_cwe.csv  UNKNOWN  ...  d847ddfe1d4475e768c547b17642d3ed0894d54e  def __call__(self, **kwargs):\n            # W...
# 
# [10 rows x 10 columns]

print("\nTRAIN UNIQUE VALUES:")
print(train.nunique())
# TRAIN UNIQUE VALUES:
# __source_file                    15
# cve_ids                          22
# cwe_ids                           1
# file_path                      5602
# label                             2
# patched_function_source       14035
# predicted_cwe_ids                41
# repo                             15
# sha                           10772
# vulnerable_function_source    14193
# dtype: int64
print("\nTEST UNIQUE VALUES:")
print(test.nunique())
# TEST UNIQUE VALUES:
# __source_file                15
# cve_ids                      15
# cwe_ids                       1
# file_path                  2225
# class                         2
# patched_function_source    3538
# predicted_cwe_ids            32
# repo                         15
# sha                        3121
# function_code              3563
# dtype: int64
## }}}

## {{{ unique values in dataset
for name, df, target in [
  ("train", train, "label"),
  ("test", test, "class"),
]:
  print(f"\n{name.upper()} DATASET:")
  print("\nClass Distribution:")
  print(df[target].value_counts(normalize=True))
  for column in [
    "__source_file",
    "cve_ids",
    "cwe_ids",
    "file_path",
    "predicted_cwe_ids",
    "repo",
    "sha",
  ]:
    print("\n")
    print(df[column].value_counts())

  print("\n" + "=" * 60)
# TRAIN DATASET:
# 
# Class Distribution:
# label
# 0    0.557973
# 1    0.442027
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_sqlmap_with_cwe.csv        841
# functions_for_airflow_with_cwe.csv       837
# functions_for_django_with_cwe.csv        832
# functions_for_salt_with_cwe.csv          826
# functions_for_ansible_with_cwe.csv       821
# functions_for_mlflow_with_cwe.csv        813
# functions_for_w3af_with_cwe.csv          719
# functions_for_tornado_with_cwe.csv       512
# functions_for_jupyter_with_cwe.csv       398
# functions_for_bandit_with_cwe.csv        351
# functions_for_volatility_with_cwe.csv    272
# functions_for_paramiko_with_cwe.csv      272
# functions_for_flask_with_cwe.csv         270
# functions_for_requests_with_cwe.csv      141
# functions_for_yaml_with_cwe.csv           45
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           14218
# CVE-2021-20191        3
# CVE-2018-16859        3
# CVE-2024-24680        2
# CVE-2022-34265        2
# CVE-2022-28346        2
# CVE-2020-11652        2
# CVE-2019-6975         2
# CVE-2020-14343        1
# CVE-2024-39330        1
# CVE-2019-14233        1
# CVE-2019-10906        1
# CVE-2021-25281        1
# CVE-2020-24584        1
# CVE-2016-2512         1
# CVE-2021-45115        1
# CVE-2021-44420        1
# CVE-2020-22935        1
# CVE-2024-39329        1
# CVE-2022-23833        1
# CVE-2024-53908        1
# CVE-2022-22936        1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    14248
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                 75
# lib/core/agent.py                                  57
# tornado/web.py                                     56
# lib/request/connect.py                             55
# tests/jobs/test_scheduler_job.py                   55
#                                                    ..
# examples/multistep_workflow/train_keras.py          1
# packaging/release.py                                1
# providers/tests/opsgenie/hooks/test_opsgenie.py     1
# airflow/operators/sensors.py                        1
# salt/modules/smbios.py                              1
# Name: count, Length: 5602, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                      3903
# CWE-Unknown                  2181
# CWE-259                       447
# CWE-89                        438
# UNKNOWN                       351
# CWE-79                        277
# CWE-330                       182
# CWE-327                       167
# CWE-605                       151
# CWE-78                        134
# CWE-94                        101
# CWE-20                         88
# CWE-22                         78
# CWE-259, CWE-703               66
# CWE-502                        65
# CWE-94, CWE-330                38
# CWE-295                        22
# CWE-22, CWE-78                 17
# CWE-327, CWE-330               17
# CWE-89, CWE-703                17
# CWE-78, CWE-703                15
# CWE-94, CWE-703                15
# CWE-330, CWE-703               12
# CWE-605, CWE-703                8
# CWE-327, CWE-703                7
# CWE-327, CWE-330, CWE-703       4
# CWE-732                         3
# CWE-94, CWE-327                 3
# CWE-20, CWE-78                  3
# CWE-89, CWE-502                 3
# CWE-89, CWE-259, CWE-703        2
# CWE-89, CWE-259                 2
# CWE-259, CWE-605                2
# CWE-22, CWE-703                 2
# CWE-78, CWE-327, CWE-330        2
# CWE-502, CWE-703                2
# CWE-259, CWE-327                1
# CWE-20, CWE-703                 1
# CWE-20, CWE-78, CWE-327         1
# CWE-295, CWE-327                1
# CWE-330, CWE-502, CWE-703       1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     2659
# saltstack/salt                     2480
# django/django                      1857
# mlflow/mlflow                      1600
# ansible/ansible                    1307
# sqlmapproject/sqlmap               1066
# andresriancho/w3af                  719
# tornadoweb/tornado                  579
# jupyter/notebook                    431
# pallets/flask                       376
# PyCQA/bandit                        351
# paramiko/paramiko                   303
# volatilityfoundation/volatility     275
# psf/requests                        195
# yaml/pyyaml                          50
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    164
# 8abdd659087504a45cf0d720c018c6ac28b3937f     62
# 9eeeff414d119c7df72b10da3dda8daf000d85ea     55
# cb295c351a016c0a10cab07f2a628b865cff3ca3     42
# df4293473d2fb6e887e31522cab5aff95e201581     40
#                                            ...
# ea55c15367536a5698b40936a9874a51a76e170a      1
# 477ffd848a9dd4326c66cb33907a2d3e010683ed      1
# ef68fd7ee91ffb156a64d06a819206747550a8a2      1
# bda01cf9939e3069837196c6b4e20314ac877d53      1
# a73eb0592c1a0893687b2313976df2d858484cf4      1
# Name: count, Length: 10772, dtype: int64
# 
# ============================================================
# 
# TEST DATASET:
# 
# Class Distribution:
# class
# 0    0.55066
# 1    0.44934
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_salt_with_cwe.csv          210
# functions_for_django_with_cwe.csv        209
# functions_for_ansible_with_cwe.csv       206
# functions_for_sqlmap_with_cwe.csv        201
# functions_for_mlflow_with_cwe.csv        199
# functions_for_airflow_with_cwe.csv       194
# functions_for_w3af_with_cwe.csv          157
# functions_for_jupyter_with_cwe.csv       121
# functions_for_tornado_with_cwe.csv       111
# functions_for_bandit_with_cwe.csv         89
# functions_for_volatility_with_cwe.csv     89
# functions_for_flask_with_cwe.csv          71
# functions_for_paramiko_with_cwe.csv       64
# functions_for_requests_with_cwe.csv       28
# functions_for_yaml_with_cwe.csv           13
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           3547
# CVE-2020-11652       2
# CVE-2019-6975        2
# CVE-2022-22936       1
# CVE-2024-41989       1
# CVE-2021-45116       1
# CVE-2019-14232       1
# CVE-2018-16859       1
# CVE-2021-25282       1
# CVE-2019-14234       1
# CVE-2024-45230       1
# CVE-2017-12794       1
# CVE-2022-34265       1
# CVE-2021-20191       1
# CVE-2024-37088       1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    3563
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                      20
# tests/admin_views/tests.py                              18
# salt/states/archive.py                                  18
# tests/test_requests.py                                  17
# lib/request/connect.py                                  14
#                                                         ..
# lib/ansible/module_utils/network/vyos/facts/facts.py     1
# lib/ansible/modules/system/filesystem.py                 1
# test/units/parsing/test_ajson.py                         1
# salt/modules/ssh.py                                      1
# tests/pytests/unit/client/ssh/test_ssh.py                1
# Name: count, Length: 2225, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                    1008
# CWE-Unknown                 514
# CWE-259                     114
# CWE-89                      101
# UNKNOWN                      89
# CWE-79                       66
# CWE-330                      55
# CWE-327                      42
# CWE-605                      40
# CWE-78                       32
# CWE-94                       25
# CWE-22                       23
# CWE-20                       21
# CWE-259, CWE-703             16
# CWE-502                      12
# CWE-94, CWE-703               6
# CWE-605, CWE-703              5
# CWE-89, CWE-703               4
# CWE-22, CWE-78                4
# CWE-295                       4
# CWE-94, CWE-330               4
# CWE-330, CWE-703              3
# CWE-94, CWE-327               3
# CWE-89, CWE-502               2
# CWE-502, CWE-703              2
# CWE-327, CWE-330              2
# CWE-78, CWE-703               2
# CWE-20, CWE-78, CWE-327       1
# CWE-22, CWE-703               1
# CWE-20, CWE-703               1
# CWE-259, CWE-605              1
# CWE-20, CWE-605               1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     680
# saltstack/salt                     600
# django/django                      490
# mlflow/mlflow                      379
# ansible/ansible                    340
# sqlmapproject/sqlmap               249
# andresriancho/w3af                 157
# jupyter/notebook                   129
# tornadoweb/tornado                 126
# pallets/flask                       99
# PyCQA/bandit                        89
# volatilityfoundation/volatility     89
# paramiko/paramiko                   71
# psf/requests                        51
# yaml/pyyaml                         14
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    39
# 8abdd659087504a45cf0d720c018c6ac28b3937f    22
# cb295c351a016c0a10cab07f2a628b865cff3ca3    13
# 9043d9dd05a3b9470abeacd9510752999a7479ae    13
# df4293473d2fb6e887e31522cab5aff95e201581    12
#                                             ..
# 3c75808c5c36a7529a93ac1bba9014907fa3e349     1
# 7eb5f532946686c7173c0d95946aa4b49c010cf1     1
# ebce47de7c72a48b7fbd0a67f0b87b906a8801c1     1
# df7338809bb4246ef028258658d049bedaaaca86     1
# cf57e487e263cc4c47f5eaf39916cb5434d720e8     1
# Name: count, Length: 3121, dtype: int64
# 
# ============================================================
## }}}

## {{{ code length
train_vul_length = train["vulnerable_function_source"].dropna().str.len()
train_patch_length = train["patched_function_source"].dropna().str.len()
print(f"\nTRAIN VULNERABLE CODE:\n{train_vul_length}")
print("\nTRAIN VULNERABLE DESCRIBE:\n", train_vul_length.describe())
print(f"\nTRAIN PATCHED CODE:\n{train_patch_length}")
print("\nTRAIN PATCHED DESCRIBE:\n", train_patch_length.describe())
print("\n" + "=" * 60)
test_vul_length = test["function_code"].dropna().str.len()
test_patch_length = test["patched_function_source"].dropna().str.len()
print(f"\nTEST VULNERABLE CODE:\n{test_vul_length}")
print("\nTEST VULNERABLE DESCRIBE:\n", test_vul_length.describe())
print(f"\nTEST PATCHED CODE:\n{test_patch_length}")
print("\nTEST PATCHED DESCRIBE:\n", test_patch_length.describe())
# TRAIN VULNERABLE CODE:
# 0         226
# 1         490
# 2        5555
# 3         734
# 4        2659
#          ...
# 14243    1703
# 14244     195
# 14245    1013
# 14246     978
# 14247     514
# Name: vulnerable_function_source, Length: 14193, dtype: int64
# 
# TRAIN VULNERABLE DESCRIBE:
#  count    14193.000000
# mean      2473.966251
# std       4420.231884
# min         31.000000
# 25%        560.000000
# 50%       1134.000000
# 75%       2415.000000
# max      47979.000000
# Name: vulnerable_function_source, dtype: float64
# 
# TRAIN PATCHED CODE:
# 0         226
# 1         487
# 2        5048
# 3         752
# 4        2660
#          ...
# 14243    1623
# 14244     195
# 14245    1066
# 14246     919
# 14247     482
# Name: patched_function_source, Length: 14147, dtype: int64
# 
# TRAIN PATCHED DESCRIBE:
#  count    14147.000000
# mean      2519.178554
# std       4429.278376
# min         31.000000
# 25%        582.000000
# 50%       1173.000000
# 75%       2496.500000
# max      47984.000000
# Name: patched_function_source, dtype: float64
# 
# ============================================================
# 
# TEST VULNERABLE CODE:
# 0       1216
# 1        293
# 2        621
# 3       7300
# 4       2163
#         ...
# 3558     286
# 3559    1377
# 3560    1628
# 3561    1067
# 3562    2633
# Name: function_code, Length: 3563, dtype: int64
# 
# TEST VULNERABLE DESCRIBE:
#  count      3563.000000
# mean       2667.377210
# std        6153.767939
# min          32.000000
# 25%         555.000000
# 50%        1126.000000
# 75%        2404.500000
# max      137703.000000
# Name: function_code, dtype: float64
# 
# TEST PATCHED CODE:
# 0        1341
# 1         280
# 2         686
# 3       11407
# 4        2175
#         ...
# 3558      435
# 3559     2019
# 3560     2914
# 3561     1164
# 3562     2639
# Name: patched_function_source, Length: 3545, dtype: int64
# 
# TEST PATCHED DESCRIBE:
#  count      3545.000000
# mean       2713.739633
# std        6179.280056
# min          32.000000
# 25%         580.000000
# 50%        1167.000000
# 75%        2481.000000
# max      137707.000000
# Name: patched_function_source, dtype: float64
#
# train histogram
fig, ax = plt.subplots()
ax.hist(train_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(train_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Training Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_histogram.png
# train box plot
fig, ax = plt.subplots()
ax.boxplot(
  [train_vul_length, train_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Training Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_boxplot.png
# test histogram
fig, ax = plt.subplots()
ax.hist(test_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(test_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Testing Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_histogram.png
# test box plot
fig, ax = plt.subplots()
ax.boxplot(
  [test_vul_length, test_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Testing Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_boxplot.png
## }}}


