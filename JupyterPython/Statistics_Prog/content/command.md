# Command

## Numpy

- `np.percentile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, interpolation=None)` : หาค่า percentile ของ array
  - `a`: array_like
  - `q`: array_like of float
  - `axis`: {int, tuple of int, None}, optional
  - `out`: ndarray, optional
  - `overwrite_input`: bool, optional
  - `interpolation`: {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}
  - `keepdims`: bool, optional

```python
np.math.comb(n, k) # หาจำนวนวิธีการเลือก k จาก n ตัว

np.math.perm(n, k) # หาจำนวนวิธีการเรียง k จาก n ตัว
```

## Pandans

### General Commands

- `croosstab(index, columns) `

### Series Commands

- `Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)

  - `normalize`: If True then the object returned will contain the relative frequencies of the unique values.
  - `sort`: Sort by values
  - `ascending`: Sort in ascending order
  - `bins`: Rather than count values, group them into half-open bins, a convenience for pd.cut, only works with numeric data.
  - `dropna`: Don’t include counts of NaN.

- `Series.mean(axis=0, skipna=True, numeric_only=False)`
- `Series.std(axis=None, skipna=True, ddof=1, numeric_only=False, **kwargs)`

### DataFrame Commands

- `DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)`

  - `n`: Number of items from axis to return. Cannot be used with frac. Default = 1 if frac = None.
  - `frac`: Fraction of axis items to return. Cannot be used with n.
  - `replace`: Sample with or without replacement. Default = False.
  - `weights`: Default 'None' results in equal probability weighting.
  - `random_state`: seed for the random number generator (if int), or numpy RandomState object.
  - `axis`: Axis to sample. Accepts axis number or name. Default is stat axis for given data type (0 for Series and DataFrames).
  - `ignore_index`: If True, the resulting axis will be labeled 0, 1, …, n - 1.

- `DataFrame.filter(items=[], like=None, regex=None, axis=None)`

- `df.sort_values(by=column_name, ascending=False, ...)`\

  - **ascending**: True = น้อยไปมาก

- `df.sort_index`
  ```
  # output
  Index(['D', 'E', 'B', 'F', 'C', 'G', 'A', 'T'], dtype='object',      name='cabin_letter')
  ```

## Scipy Commands

_**\*Scipy - stats (import)**_

**Method ที่ใช้บ่อยใน คัวแปรสุ่มแบบไม่ต่อเนื่องและแบบต่อเนื่อง**

```python
def pmf(x, loc=0, *args, **kwds): # : Probability mass function at x of the given RV.
def cdf(x, loc=0, *args, **kwds): #: ฟังก์ชันการกระจายสะสม (Cumulative distribution function) ที่ x ของ RV ที่กำหนด
def ppf(q, loc=0, *args, **kwds): #: inverse of cdf (เป็นฟังก์ชันที่ใช้ในการหาค่าที่เป็นไปได้ของตัวแปรสุ่ม )
def sf(x, loc=0, *args, **kwds): #: Survival function (also defined as _1 - cdf_, but sf is sometimes more accurate).
def isf(q, loc=0, *args, **kwds): #: Inverse survival function (inverse of sf).
```

|

```python
stats.binom.pmf(k, n, p, loc=0) #คำนวณความน่าจะเป็นของการเกิดเหตุการณ์ที่เป็นไปได้ทั้งหมด
```

- `k`: จำนวนครั้งที่เกิดเหตุการณ์ที่สนใจ
- `n`: จำนวนครั้งที่เกิดเหตุการณ์ทั้งหมด
- `p`: ความน่าจะเป็นของเหตุการณ์ที่สนใจ
- `loc`: ค่าเริ่มต้นของการกระจาย

```python
stats.poisson.pmf(k, mu, loc=0)
```

- `k`: จำนวนครั้งที่เกิดเหตุการณ์ที่สนใจ
- `mu`: ค่าคาดหมายของการเกิดเหตุการณ์ที่สนใจ
- `loc`: ค่าเริ่มต้นของการกระจาย

```python
cumu_p = 0.95
df = 10 # degree of freedom (v)
ppf_v = stats.t.ppf(cumu_p, df, loc=0, scale=1)#: Percent point function (inverse of cdf — percentiles).
stats.t.cdf(x, df, loc=0, scale=1)#: Cumulative distribution function.
stats.t.sf(x, df, loc=0, scale=1)#: Survival function (1 - cdf — sometimes more accurate).
stats.t.isf(1-cumu_p, df, loc=0, scale=1)#: Inverse survival function (inverse of sf).
```

# Midterm exam Guide

### 1. ความหมายของประชากรและตัวอย่าง

- ประชากร (Population) คือ ชุดของสิ่งที่เราสนใจที่จะศึกษา หรือที่เราต้องการทราบข้อมูล
- ตัวอย่าง (Sample) คือ สิ่งที่เราสนใจที่เราสามารถเก็บข้อมูลได้ และเป็นส่วนหนึ่งของประชากร

### 2. สถิตเชิงพรรณนา (Descriptive Statistics) และ อนุมาน คืออะไร

- **สถิติเชิงพรรณนา** (Descriptive Statistics)

  - การอธิบายข้อมูลที่มีอยู่ในตัวอย่าง โดยใช้ตัวเลข กราฟ visualization หรือ ตาราง \
  - วิเคราะห์ข้อมูลด้วนการคำนซณค่าางสถิติต่างๆ เช่น mean SD (standard deviation) หรือ ค่าสถิติที่เกี่ยวข้องอื่นๆ etc.\

- **สถิติเชิงการอนุมาน** (Inferential Statistics)
  - การใช้ข้อมูลที่มีอยู่ในตัวอย่าง มาอนุมานถึงประชากรที่เราสนใจ
  - นำทฤษฎีสถิติมาใช้ในการตัดสินใจ วิเคราะห์ข้อมูล หรือการทำนายเกี่ยวกับประชากร จาก sample
  - นิยมใช้ ทดสอบสมมุติฐาน (Hypothesis Testing) และ การสร้างแบบจำลอง (Modeling) วิเคราะห์ขความแปรปวน

### 3. รูปแบบการสุ่มตัวอย่าง

- **Simple Random Sampling** การสุ่มตัวอย่างแบบสุ่มง่าย
  - การสุ่มตัวอย่างมีความน่าจะเป็นเท่ากันทุกตัวอย่าง
- **สุ่มแบบเป็นระบบ** : เลือกตัวอย่างจากประชากรที่เรียงกันอยู่โดยมีการกำหนดจุดเริ่มต้นและขนาดของช่วงการสุ่ม
  - สุ่มแบบเป็นระบบแบ่งออกเป็น 2 ประเภท
    - สุ่มแบบเป็นระบบแบบไม่มีการกำหนดขนาดตัวอย่าง
    - สุ่มแบบเป็นระบบแบบมีการกำหนดขนาดตัวอย่าง
- **สุ่มแบบชั้นภูมิ** : การสุ่มตัวอย่างโดยการแบ่งประชากรออกเป็นชั้นภูมิ แล้วสุ่มตัวอย่างจากแต่ละชั้นภูมิ
- **สุ่มแบบกลุ่ม** : เลือกสุ่มมาจำนวนหนึ่ง เพื่อเป็นตัวแทนจอวประชากร
- **สุ่มแบบหลายขั้นตอน** : เป็นการ sub sampling โดยมาการสุ่มย่อยมากกว่า 2 ขั้น
