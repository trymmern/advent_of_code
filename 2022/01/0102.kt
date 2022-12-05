import java.io.File

fun main() {
    var max = arrayOf(0, 0, 0)
    var counter: Int = 0
    var cont: Boolean = false
    
    File("input.txt").forEachLine { it ->
        if (it.isEmpty()) {
            if (max.any{it2 -> it2 < counter}) {
                max[max.indexOf(max.min())] = counter
            }
            counter = 0
            cont = true
        }
        if (!cont) {
            counter += it.toInt()
        }
        cont = false
    }
    println(max.sum())
}