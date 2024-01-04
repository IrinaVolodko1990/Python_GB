
# int[,] matrix = new int[number, number];  задача по таблице умножения

# for (int i = 0; i < number; i++)
# {
#     for (int j = i; j < number; j++)
#     {
#         matrix[i, j] = (i + 1) * (j + 1);
#         matrix[j, i] = (i + 1) * (j + 1);
#     }
# }

# for (int i = 0; i < number; i++)
# {
#     for (int j = 0; j < number; j++)
#     {
#         Console.Write(matrix[i, j]);
#         Console.Write("\t");
#     }
#     Console.WriteLine();
# }