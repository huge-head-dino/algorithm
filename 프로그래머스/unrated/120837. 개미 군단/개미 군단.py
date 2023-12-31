def solution(hp):
    answer = 0
    general = hp // 5
    g_rest = hp % 5
    soldier = g_rest % 3
    s_rest = g_rest // 3
    answer = general + soldier + s_rest
    return answer