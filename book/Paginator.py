from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 分页器


def mypaginator(book_list, current_page_num, show_data_num, show_page_num):
    paginator = Paginator(book_list, show_data_num)   # 要分页的对象
    all_page_num = paginator.num_pages                # 总共的page数量
    half_page = int(show_page_num / 2)

    try:
        current_page = paginator.page(current_page_num)   # 当前页码总共要显示的obj对象
    except EmptyPage:                       # http://127.0.0.1:8000/app01/blog/?page=-22
        current_page = paginator.page(1)
    except PageNotAnInteger:                # http://127.0.0.1:8000/app01/blog/?dafdsaf
        current_page = paginator.page(1)

    if all_page_num > show_page_num:
        if current_page_num < half_page + 1:
            page_range = range(1, show_page_num + 1)
            print('头部', page_range)
        elif current_page_num > all_page_num - half_page:
            page_range = range(all_page_num - show_page_num + 1, all_page_num + 1)
            print('尾部', page_range)
        else:
            page_range = range(current_page_num - half_page, current_page_num + half_page + 1)
            print('中间', page_range)
    else:
        page_range = range(1, all_page_num + 1)
        print('1', page_range)

    return page_range, current_page