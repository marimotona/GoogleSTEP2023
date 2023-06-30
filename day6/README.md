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
フリーリストのすべてのブロックを走査し、現在のブロックが要求サイズと一致するか、</br>
またはそれ以上であるかを確認する。</br>
もし、best_metsdataがNULLか、現在のmetadataのサイズがこれまで見つけた最良のブロックよりも</br>
小さい場合、best_metadataと、best_prevを更新する。</br>


### worst_fit
![スクリーンショット 2023-06-29 194433](https://github.com/marimotona/GoogleSTEP2023/assets/105051587/7b564583-1cc3-4a19-a8ea-9a0e8c386bc7)</br>
すごい時間がかかっている、、、

```c
  my_metadata_t *metadata = my_heap.free_head;
  my_metadata_t *prev = NULL;
  my_metadata_t *worst_metadata = NULL;
  my_metadata_t *worst_prev = NULL;

  while(metadata) {
        if (metadata->size >= size) {
            if (worst_metadata == NULL || worst_metadata->size < metadata->size) {
                worst_metadata = metadata;
                worst_prev = prev;
            }
        }
        prev = metadata;
        metadata = metadata->next;
    }

    metadata = worst_metadata;
    prev = worst_prev;
```
ブロックよりもサイズが大きいフリーメモリブロックの中で、最も大きいサイズのものを探す

### free_list_bin
![スクリーンショット 2023-06-30 140607](https://github.com/marimotona/GoogleSTEP2023/assets/105051587/ac6ca229-6700-476e-954e-96e8c7ff9a21)
```c
typedef struct my_metadata_t {
  size_t size;
  int bin_index;
  struct my_metadata_t *next;
} my_metadata_t;

#define NUM_BINS 5
#define BIN_SIZE 1000  

typedef struct my_heap_t {
  my_metadata_t *free_head[NUM_BINS];
  my_metadata_t dummy;
} my_heap_t;

void my_add_to_free_list(my_metadata_t *metadata) {
  assert(!metadata->next);
  int index = metadata->size / BIN_SIZE;
  metadata->bin_index = index;
  metadata->next = my_heap.free_head[index];
  my_heap.free_head[index] = metadata;
}

void my_remove_from_free_list(my_metadata_t *metadata, my_metadata_t *prev) {
  int index = metadata->bin_index;
  if (prev) {
    prev->next = metadata->next;
  } else {
    my_heap.free_head[index] = metadata->next;
  }
  metadata->next = NULL;
}

void my_initialize() {
    for (int i = 0; i < NUM_BINS; ++i) {
        my_heap.free_head[i] = &my_heap.dummy;
    }
    my_heap.dummy.size = 0;
    my_heap.dummy.next = NULL;
}

void *my_malloc(size_t size) {
  int start_index = size / BIN_SIZE;
  my_metadata_t *best_metadata = NULL;
  my_metadata_t *best_prev = NULL;

  for(int i = start_index; i < NUM_BINS; i++) {
    my_metadata_t *metadata = my_heap.free_head[i];
    my_metadata_t *prev = NULL;

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
    if (best_metadata) break;
   }

  if (!best_metadata) {
    size_t buffer_size = 4096;
    my_metadata_t *metadata = (my_metadata_t *)mmap_from_system(buffer_size);
    metadata->size = buffer_size - sizeof(my_metadata_t);
    metadata->next = NULL;

    my_add_to_free_list(metadata);

    return my_malloc(size);
  }


  void *ptr = best_metadata + 1;
  size_t remaining_size = best_metadata->size - size;

  my_remove_from_free_list(best_metadata, best_prev);

  if (remaining_size > sizeof(my_metadata_t)) {
    best_metadata->size = size;

    my_metadata_t *new_metadata = (my_metadata_t *)((char *)ptr + size);
    new_metadata->size = remaining_size - sizeof(my_metadata_t);
    new_metadata->next = NULL;

    my_add_to_free_list(new_metadata);
  }
  return ptr;
}


void my_free(void *ptr) {
  my_metadata_t *metadata = (my_metadata_t *)ptr - 1;
  metadata->next = NULL;
  my_add_to_free_list(metadata);
}
```
