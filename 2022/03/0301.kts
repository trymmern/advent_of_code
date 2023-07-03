import java.io.File

fun main() {
    var values = getValues()
    println(values)
    
    var score = 0
    File("input.txt").forEachLine { it ->
        var str1 = it.substring(0, it.length/2)
        var str2 = it.substring(it.length/2, it.length)

        var cont: Boolean = false
        for (i in 0 until str1.length) {
            for (j in 0 until str2.length) {
                if (str1[i] == str2[j]) {
                    score += values.get(str1[i])!!
                    cont = true
                    break
                }
            }
            if (cont) break
        }
    }

    println(score)
}

fun getValues(): Map<Char, Int> {
    var lc = mutableMapOf<Char, Int>()
    var lowercase: Char = 'a'
    var index: Int = 1
    while (lowercase <= 'z') {
        lc.put(lowercase, index)
        index++
        ++lowercase
    }
    
    var uc = mutableMapOf<Char, Int>()
    var uppercase: Char = 'A'
    while (uppercase <= 'Z') {
        uc.put(uppercase, index)
        index++
        ++uppercase
    }

    return lc + uc
}

main()