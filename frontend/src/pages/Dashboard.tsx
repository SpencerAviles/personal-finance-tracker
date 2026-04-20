import { useEffect, useState } from "react";
import { CategorySummary, MonthlyTotal, getSpendingByCategory, getMonthlyTotals } from "@/api/transactions";
import SpendingPieChart from "@/components/charts/SpendingPieChart";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function Dashboard() {
  const [categoryData, setCategoryData] = useState<CategorySummary[]>([]);
  const [monthlyData, setMonthlyData] = useState<MonthlyTotal[]>([]);

  useEffect(() => {
    // TODO: Fetch spending by category and monthly totals on mount
    // TODO: Store results in state
  }, []);

  // TODO: Calculate total spending this month from monthlyData
  // TODO: Find the top spending category from categoryData

  return (
    <div>
      {/* TODO: Summary cards — total spent this month, top category */}
      {/* TODO: SpendingPieChart component with categoryData */}
      {/* TODO: Month filter (select dropdown) to change which month is shown */}
      <h1>Dashboard</h1>
    </div>
  );
}
