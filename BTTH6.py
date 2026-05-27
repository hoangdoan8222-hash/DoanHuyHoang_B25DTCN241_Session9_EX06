branch_names = [
    "Highlands Nhà Thờ",
    "Highlands Bà Triệu",
    "Highlands Nguyễn Du",
    "Highlands Landmark 81",
    "Highlands Trần Hưng Đạo"
]

daily_revenues = [
    15500000,
    28000000,
    9200000,
    45000000,
    11000000
]

target_achieved = [
    True,
    True,
    False,
    True,
    False
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém")
    print("4. Thoát chương trình")
    print("================================================")

    try:
        choice = int(input("Nhập lựa chọn của bạn (1-4): "))

        match choice:

            case 1:

                print("\n===== BÁO CÁO DOANH THU =====")
                print(f"{'CHI NHÁNH':30}{'DOANH THU':20}{'TRẠNG THÁI'}")

                for i in range(len(branch_names)):
                    status = "Đạt" if target_achieved[i] else "Không Đạt"

                    print(
                        f"{branch_names[i]:30}"
                        f"{daily_revenues[i]:,} VNĐ"
                        f"{'':5}{status}"
                    )

                print("-" * 65)
                print("Tổng doanh thu:", f"{sum(daily_revenues):,} VNĐ")

            case 2:

                max_revenue = max(daily_revenues)
                min_revenue = min(daily_revenues)

                max_index = daily_revenues.index(max_revenue)
                min_index = daily_revenues.index(min_revenue)

                print("\nChi nhánh doanh thu cao nhất:")
                print(branch_names[max_index], "-", f"{max_revenue:,} VNĐ")

                print("\nChi nhánh doanh thu thấp nhất:")
                print(branch_names[min_index], "-", f"{min_revenue:,} VNĐ")

            case 3:

                failed_branches = []

                for i in range(len(branch_names)):
                    if target_achieved[i] == False:
                        failed_branches.append(branch_names[i])

                print("\nDanh sách cơ sở không đạt:")
                print(failed_branches)

            case 4:

                print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
                break

            case _:

                print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại!")

    except ValueError:

        print("[Lỗi] Vui lòng nhập số từ 1 đến 4!")