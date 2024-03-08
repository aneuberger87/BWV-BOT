import { Suspense } from "react";
import { getAllCompanies } from "../../lib/fetches";
import { FaCheck, FaExclamationTriangle, FaTimes, FaCog } from "react-icons/fa";
import { excelExists } from "@/lib/action-excel-exists";

const StatusEmote = ({
  status,
}: {
  status: "done" | "pending" | "error" | "none";
}) => {
  switch (status) {
    case "done":
      return <FaCheck style={{ color: "green" }} />;
    case "pending":
      return <FaCog style={{ color: "grey" }} />;
    case "error":
      return <FaExclamationTriangle style={{ color: "orange" }} />;
    default:
      return <FaTimes style={{ color: "red" }} />;
  }
};

const ListTask = async () => {
  const companies = excelExists("companiesList");
  const students = excelExists("studentsList");
  const rooms = excelExists("roomsList");
  return (
    <div className="grid grid-cols-[auto_1fr] items-center gap-2">
      <div className="col-span-2"></div>
      <StatusEmote status={rooms ? "done" : "none"} />
      <span>
        Hochgeladen: <span className="font-mono text-lg">Raumdaten</span>
      </span>
      <StatusEmote status={companies ? "done" : "none"} />
      <span>
        Hochgeladen: <span className="font-mono text-lg">Firmendaten</span>
      </span>
      <StatusEmote status={students ? "done" : "none"} />
      <span>
        Hochgeladen: <span className="font-mono text-lg">Schülerdaten</span>
      </span>
      <div className="col-span-2 h-2"></div>
      <StatusEmote status={students ? "done" : "none"} />
      <span>
        Verlosung: <span className="font-mono text-lg">Firmen aufgeteilt</span>
      </span>
      <StatusEmote status={students ? "done" : "none"} />
      <span>
        Verlosung: <span className="font-mono text-lg">Schüler aufgeteilt</span>
      </span>
    </div>
  );
};

const ListSuspense = () => {
  return (
    <Suspense fallback={<div>Loading</div>}>
      <ListTask />
    </Suspense>
  );
};

export default ListSuspense;
