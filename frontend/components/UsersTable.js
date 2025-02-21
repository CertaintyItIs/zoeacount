"use client";

import { useCallback, useState } from "react";
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  Chip,
  Tooltip,
  useDisclosure,
  Button,
} from "@heroui/react";

import DeleteIcon from "./icons/DeleteIcon";
import EditIcon from "./icons/EditIcon";
import PasswordIcon from "./icons/PasswordIcon";
import UserInfoModal from "./modals/UserInfoModal";
import ChangePasswordModal from "./modals/ChangePasswordModal";
import RegisterUserModal from "./modals/RegisterUserModal"; // Import Register Modal

const dateOptions = {
  year: "numeric",
  month: "long",
  day: "numeric",
};

const statusColorMap = {
  admin: "bg-orange-500",
  staff: "bg-orange-200",
};

export default function UsersTable({ columns, users }) {
  const changePassModal = useDisclosure();
  const editModal = useDisclosure();
  const registerUserModal = useDisclosure(); // Modal for Register User

  const [userDetails, setUserDetails] = useState();
  const [selectedKeys, setSelectedKeys] = useState(new Set([]));

  const openEditModal = (id, username, role) => {
    editModal.onOpen();
    setUserDetails([{ id, username, role }]);
    setSelectedKeys(new Set([role]));
  };

  const renderCell = useCallback((user, columnKey) => {
    const cellValue = user[columnKey];

    switch (columnKey) {
      case "date_joined":
        return new Date(cellValue).toLocaleDateString("en-US", dateOptions);
      case "last_login":
        return cellValue ? (
          new Date(cellValue).toLocaleDateString("en-US", dateOptions)
        ) : (
          <p className="active:opacity-50">Not yet logged in</p>
        );
      case "role":
        return (
          <Chip
            className={`capitalize ${statusColorMap[user.role]} `}
            size="sm"
            variant="flat"
          >
            {cellValue}
          </Chip>
        );
      case "actions":
        return (
          <div className="relative flex items-center gap-2">
            <Tooltip content="Edit user">
              <span className="text-lg text-default-400 cursor-pointer active:opacity-50">
                <Button isIconOnly onPress={() => openEditModal(user.id, user.username, user.role)}>
                  <EditIcon />
                </Button>
              </span>
            </Tooltip>
            <Tooltip content="Change password">
              <span className="text-lg text-danger cursor-pointer active:opacity-50">
                <Button isIconOnly onPress={() => changePassModal.onOpen()}>
                  <PasswordIcon />
                </Button>
              </span>
            </Tooltip>
            <Tooltip color="danger" content="Delete user">
              <span className="text-lg text-danger cursor-pointer active:opacity-50">
                <Button color="danger" isIconOnly>
                  <DeleteIcon />
                </Button>
              </span>
            </Tooltip>
          </div>
        );
      default:
        return cellValue;
    }
  }, []);

  return (
    <>
      {/* Register New User Button */}
      <div className="flex justify-end mb-4">
        <Button color="primary" onPress={registerUserModal.onOpen}>
          Register New User
        </Button>
      </div>

      {/* Users Table */}
      <Table>
        <TableHeader columns={columns}>
          {(column) => (
            <TableColumn key={column.uid} align="start">
              {column.name}
            </TableColumn>
          )}
        </TableHeader>
        <TableBody items={users}>
          {(item) => (
            <TableRow key={item.id}>
              {(columnKey) => (
                <TableCell>{renderCell(item, columnKey)}</TableCell>
              )}
            </TableRow>
          )}
        </TableBody>
      </Table>

      {/* Modals */}
      <UserInfoModal
        isOpen={editModal.isOpen}
        onOpenChange={editModal.onOpenChange}
        userDetails={userDetails}
        selectedKeys={selectedKeys}
        setSelectedKeys={setSelectedKeys}
      />

      <ChangePasswordModal
        isOpen={changePassModal.isOpen}
        onOpenChange={changePassModal.onOpenChange}
      />

      <RegisterUserModal
        isOpen={registerUserModal.isOpen}
        onOpenChange={registerUserModal.onOpenChange}
      />
    </>
  );
}
