def count_by_extension(paths: list[str]) -> dict[str, int]:
    count = {}
    for path in paths:
        file = path.rsplit('/', 1)[-1]
        if '.' in file:
            ras = file.rsplit('.', 1)[1].lower()
        else:
            ras = ''
        count[ras] = counts.get(ras, 0) + 1
    return count

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ''
    else:
        mx = paths[0]
        mx_slash = mx.count('/')
        for p in paths[1:]:
            slash = p.count('/')
            if slash > mx_slash:
                mx_slash = slash
                mx = p
            elif slash == mx_slash and p < mx:
                mx = p
    return mx

