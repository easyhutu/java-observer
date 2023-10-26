### 代码变更依赖检查工具-观察者

---

* git diff commit-id1 commit-id2 --stat
    * 分析出修改影响的方法
    * 收集所有的方法保存在diffStat类中

---

* 扫描项目入口目录下的所有Java文件
* 依次解析所有的Java文件构建语法树
* 递归遍历引用链路

---

* 将所有的引用链路统计渲染到HTML静态页面中

### 运行命令

```shell
python run.py --m *path*
```