import { Suspense } from "react";
import { getAllCompanies } from "../../lib/fetches";
import { FaCheck, FaExclamationTriangle, FaTimes, FaCog } from "react-icons/fa";
import { excelExists } from "@/lib/excel-exists";
import { getDataStatusCachable } from "@/lib/data-status";

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
  const data = getDataStatusCachable();
  const rooms = data.input.excel.roomsExist;
  const companies = data.input.excel.companiesExist;
  const students = data.input.excel.studentsExist;

  const calculated = data.output.calculated;

  const downloadedRooms = data.output.downloaded.rooms;
  const downloadedCompanies = data.output.downloaded.companies;
  const downloadedStudents = data.output.downloaded.students;
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
      <div className="col-span-2 h-2" />
      <StatusEmote status={calculated ? "done" : "none"} />
      <span>
        Berechnet: <span className="font-mono text-lg">Eventaufteilung</span>
      </span>
      {/* <div className="col-span-2 h-2" />
      <StatusEmote status={downloadedRooms ? "done" : "none"} />
      <span>
        Heruntergeladen: <span className="font-mono text-lg">Raumdaten</span>
      </span>
      <StatusEmote status={downloadedCompanies ? "done" : "none"} />
      <span>
        Heruntergeladen: <span className="font-mono text-lg">Firmendaten</span>
      </span>
      <StatusEmote status={downloadedStudents ? "done" : "none"} />
      <span>
        Heruntergeladen: <span className="font-mono text-lg">Schülerdaten</span>
      </span> */}
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
