import api from "./client";

export interface Transaction {
  id: number;
  date: string;
  description: string;
  amount: number;
  category: string;
  bank_name: string;
  hash: string;
}

export interface CategorySummary {
  category: string;
  total: number;
}

export interface MonthlyTotal {
  year: number;
  month: number;
  total: number;
}

export async function getTransactions(params?: {
  month?: number;
  year?: number;
  bank_name?: string;
  category?: string;
}): Promise<Transaction[]> {
  try {
    const response = await api.get("/transactions", { params });
    return response.data;
  }
  catch (error) {
    console.error("Error fetching transactions:", error);
    throw error;
  }
}

export async function updateTransactionCategory(
  id: number,
  category: string
): Promise<Transaction> {
  try {
    const response = await api.patch(`/transactions/${id}`, { category });
    return response.data;
  }
  catch (error) {
    console.error(`Error updating transaction ${id}:`, error);
    throw error;
  }
}

export async function getSpendingByCategory(params?: {
  month?: number;
  year?: number;
}): Promise<CategorySummary[]> {
  try {
    const response = await api.get("/summary/by-category", { params });
    return response.data;
  }
  catch (error) {
    console.error("Error fetching category summary:", error);
    throw error;
  }
}

export async function getMonthlyTotals(params?: {
  year?: number;
}): Promise<MonthlyTotal[]> {
  try {
    const response = await api.get("/summary/monthly", { params });
    return response.data;
  }
  catch (error) {
    console.error("Error fetching monthly totals:", error);
    throw error;
  }
}

export async function uploadCSV(
  file: File,
  bank: string,
  bankName: string
): Promise<{ inserted: number; duplicates_skipped: number }> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("bank", bank);
  formData.append("account_name", bankName);
  try {
    const response = await api.post("/upload", formData);
    return response.data;
  }
  catch (error) {
    console.error("Error uploading CSV:", error);
    throw error;
  }
}

export async function deleteTransaction(
  hash: string
): Promise<void> {
  try {
    await api.delete(`/transactions/${hash}`);
  }
  catch (error) {
    console.error(`Error deleting transaction with hash ${hash}:`, error);
    throw error;
  }
}
