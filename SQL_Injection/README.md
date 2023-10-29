# SQL Injection - 了解原理

## SQL Injection (SQLi) 是一種典型的應用程式安全的漏洞，透過它，攻擊者可以操縱或更改 SQL 查詢的原本意圖。在這段 PHP 代碼中，這個問題主要是因為直接使用用戶輸入的數據（未經過任何檢查或過濾）在 SQL 查詢中。

### WriteUp
當輸入 admin' -- 作為用戶名，並帶有任何密碼，實際上是在做以下的事情：

原始的 SQL 查詢是：
```sql
SELECT * FROM users WHERE username='[USERNAME]' AND password='[PASSWORD]'
```
如果將 [USERNAME] 替換為 admin' -- 和 [PASSWORD] 替換為任何密碼，查詢會變成：
```sql
SELECT * FROM users WHERE username='admin' --' AND password='[PASSWORD]'
```
這裡的 -- 是 SQL 的單行註釋符號。因此，這會使 SQL 從原始的比較變成只對用戶名進行比較，而忽略密碼部分，使得攻擊者無需知道真實的密碼。

由於資料庫中存在一個用戶名為 admin 的用戶，所以查詢會返回該用戶的資料，從而使得攻擊者登入成功。

### 使用 OR 進行 SQL Injection

除了上面描述的方法，攻擊者還可以使用 OR 進行 SQL 注入來繞過認證。當攻擊者不知道具體的用戶名時，他們可以使用 OR 子句以確保查詢的結果始終為真。

舉例如下：

當輸入 anything' OR '1' = '1 -- 作為用戶名，且密碼為任意值時，原始的 SQL 查詢會被更改如下：

原始查詢：
```sql
SELECT * FROM users WHERE username='[USERNAME]' AND password='[PASSWORD]'
```
替換 [USERNAME] 後的查詢：
```sql
SELECT * FROM users WHERE username='anything' OR '1' = '1' --' AND password='[PASSWORD]'
```
由於 '1' = '1' 永遠為真，這意味著這次查詢會返回第一個用戶的資料，通常這是管理員賬號。這樣，即使攻擊者不知道用戶名，他們也可以登入。

為了預防這類攻擊，應用程式應該使用參數化查詢或準備語句，並且從不直接將用戶輸入的數據插入到 SQL 查詢中。
