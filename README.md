# DCL-160: Python Programming

These projects are created as part of the following training: DCL-160 "Python Programming"

Please follow the link for the complete training catalog: https://www.deepcloudlabs.com/resources

# Module 10 - Modules and Packages

Python'da bir paket oluşturmak için bir dizin yaratmanız yeterli olacaktır:

![Installation folder](module10-figure01.png?raw=true "package directory content")

Bu dizin yapısı içinde **`__init__.py`** dosyası modül yüklenirken bir kere çalıştırılır ve modülle ilgili başlangıç işlemleri gerçekleştirilir:

```python
print("deepcloudlabs module is loaded!")
# all initialization code goes here

from deepcloudlabs.dictionary import lines

with open("deepcloudlabs/dictionary-tur.txt", "r") as the_file:
    for line in the_file.readlines():
        lines.append(line.strip())
```

Böylelikle modül içindeki **dictionary.py** dosyası içinde tekrar tekrar dosyanın yüklenmesine gerek olmaz:


```python
lines = []

def get_word(index):
    return lines[index]
```

Burada **lines** listesi her zaman modül yüklenirken sözlük dosyası okunarak doldurulur. Modülün kullanımına ilişkin aşağıdaki örneklere göz atalım:

```python
from deepcloudlabs.utils import lost_numbers as nums, is_even as cift_mi

print(nums)
print(cift_mi(42))

import deepcloudlabs.hr

print(dir(deepcloudlabs))
example = {
    "identity": "9876543210",
    "fullname": "kate austen"
}
jack = deepcloudlabs.hr.Employee("12345678910", "jack bauer")

kate = deepcloudlabs.hr.Employee(**example)

print(jack.identity, jack.fullname)
print(kate.identity, kate.fullname)

from deepcloudlabs.dictionary import get_word

print(get_word(42))
```

**deepcloudlabs** altındaki **utils.py** paketini yüklemek için aşağıdaki python satırını yazmanız yeterli olacaktır:

```python
from deepcloudlabs.utils import lost_numbers as nums, is_even as cift_mi
```

**deepcloudlabs** altındaki **hr.py** paketini yüklemek için aşağıdaki python satırını yazmanız yeterli olacaktır:

```python
import deepcloudlabs.hr
```

Bu şekilde **Employee** sınıfından nesne yaratabilirsiniz:

```python
example = {
    "identity": "9876543210",
    "fullname": "kate austen"
}
jack = deepcloudlabs.hr.Employee("12345678910", "jack bauer")

kate = deepcloudlabs.hr.Employee(**example)

print(jack.identity, jack.fullname)
print(kate.identity, kate.fullname)
```
Sözlükteki 42. sıradaki kelimeye erişmek için ise aşağıdaki kodu yazıyoruz:

```python
from deepcloudlabs.dictionary import get_word

print(get_word(42))
```
