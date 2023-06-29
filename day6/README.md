# MALLOC CHALLENGE
1. mallocの実装</br>
2. 100マス計算

## Cポインタ100マス計算
<img src="https://github.com/marimotona/GoogleSTEP2023/assets/105051587/885f06f0-4004-4f27-828f-ea0fff6a9d00" width="600px">

## mallocの実装

### best_fit
![スクリーンショット 2023-06-29 174004](https://github.com/marimotona/GoogleSTEP2023/assets/105051587/994c9483-f2bf-4bd1-8c47-c33f4597c281)

```c
  my_metadata_t *metadata = my_heap.free_head;
  my_metadata_t *prev = NULL;
  my_metadata_t *best_metadata = NULL;
  my_metadata_t *best_prev = NULL;

    while(metadata) {
        if (metadata->size >= size) {
            if (best_metadata == NULL || best_metadata->size > metadata->size) {
                best_metadata = metadata;
                best_prev = prev;
            }
        }
        prev = metadata;
        metadata = metadata->next;
    }

    metadata = best_metadata;
    prev = best_prev;
```
