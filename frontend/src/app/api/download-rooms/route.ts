import { downloadInputExcelAsBuffer } from "@/lib/download";

export const GET = async () => {
  const buffer = await downloadInputExcelAsBuffer("roomsList");
  if (buffer === null)
    return new Response("File does not exist", { status: 404 });

  return new Response(buffer, {
    headers: {
      "Content-Type": "application/octet-stream",
      "Content-Disposition": `attachment; filename="roomsList.xlsx"`,
    },
  });
};

export const dynamic = "force-dynamic";
