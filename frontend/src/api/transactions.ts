import api from "./client";

export interface Transaction {
  id: number;
  date: string;
  description: string;
  amount: number;
  category: string;
  account: string;
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
  account?: string;
}): Promise<Transaction[]> {
  // TODO: GET /transactions with optional query params
  // TODO: Return the response data
  return [];
}

export async function updateTransactionCategory(
  id: number,
  category: string
): Promise<Transaction> {
  // TODO: PATCH /transactions/:id with { category }
  // TODO: Return the updated transaction
  return {} as Transaction;
}

export async function getSpendingByCategory(params?: {
  month?: number;
  year?: number;
}): Promise<CategorySummary[]> {
  // TODO: GET /summary/by-category with optional query params
  // TODO: Return the response data
  return [];
}

export async function getMonthlyTotals(params?: {
  year?: number;
}): Promise<MonthlyTotal[]> {
  // TODO: GET /summary/monthly with optional query params
  // TODO: Return the response data
  return [];
}

export async function uploadCSV(
  file: File,
  bank: string,
  accountName: string
): Promise<{ inserted: number; duplicates_skipped: number }> {
  // TODO: Build a FormData object with file, bank, and account_name
  // TODO: POST /upload with the FormData
  // TODO: Return the response data
  return { inserted: 0, duplicates_skipped: 0 };
}
